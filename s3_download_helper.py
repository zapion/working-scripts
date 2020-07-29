import aiobotocore
import asyncio
import aiofiles



def main():
    # This list is data got from s3 ls command
    filelist = ""
    with open(filelist) as inp:
        lis = inp.readlines()
        records = list(map(lambda x: x.split(' ')[-1], lis))
        # asyncio.run(execute(records))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(execute(records))
        finally:
            loop.close()
            asyncio.set_event_loop(None)

async def execute(records):
    slice_cnt = 10
    prefix = 'any_key/'
    bucket = 'bucket name'
    async def send(fns):
        session = aiobotocore.get_session()
        async with session.create_client(
            's3',
            region_name='ap-northeast-1',
        ) as client:
            for fn in fns:
                fi = prefix + fn.strip()
                # print(fi)
                try:
                    async with aiofiles.open(fn.strip(), 'wb') as data:

                        resp = await client.get_object(
                            Bucket=bucket,
                            Key=fi,
                        )
                        async with resp['Body'] as stream:
                            content = await stream.read()
                            await data.write(content)
                except FileNotFoundError as e:
                    print(e)
            return
    for i in range(0, len(records), slice_cnt):
        await send(records[i:i+slice_cnt])
    return


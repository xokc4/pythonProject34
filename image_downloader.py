import os
import requests
import time
import threading
import multiprocessing
import asyncio
import aiohttp
import argparse

# Функция для скачивания изображения с использованием многопоточности
def download_image_thread(url):
    filename = os.path.basename(url)
    response = requests.get(url)
    with open("MultithreadedFile/"+filename, 'wb') as f:
        f.write(response.content)
    print(f"Загрузка {filename}")

# Функция для скачивания изображения с использованием Многопроцессорный
def download_image_Multiprocessor(url):
    filename = os.path.basename(url)
    response = requests.get(url)
    with open("MultiprocessorFile/"+filename, 'wb') as f:
        f.write(response.content)
    print(f"Загрузка {filename}")

# Функция для скачивания изображения с использованием асинхронности
async def download_image_async(url, session):
    filename = os.path.basename(url)
    async with session.get(url) as response:
        with open("AsynchronousFile/"+filename, 'wb') as f:
            f.write(await response.read())
    print(f"Загрузка {filename}")

async def main_async(urls):
    await asyncio.sleep(1)
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(url, session) for url in urls]
        await asyncio.gather(*tasks)

def Multithreaded():
    start_time = time.time()
    threads = []
    for url in args.urls:
        t = threading.Thread(target=download_image_thread, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"Время загрузки: {end_time - start_time} секунды")

def Multiprocessor():
    start_time = time.time()
    processes = []
    for url in args.urls:
        p = multiprocessing.Process(target=download_image_Multiprocessor, args=(url,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end_time = time.time()
    print(f"Время загрузки: {end_time - start_time} секунды")

def Asynchronous():
    start_time = time.time()

    asyncio.get_event_loop().run_until_complete(main_async(args.urls))
    end_time = time.time()
    print(f"Время загрузки: {end_time - start_time} секунды")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image downloader')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='List of image URLs')
    args = parser.parse_args()

    # Многопоточный подход
    Multithreaded()

    Multiprocessor()

    Asynchronous()
# запуск
# python image_downloader.py https://ratatum.com/wp-content/uploads/2018/11/7-17-1.jpg https://vraki.net/sites/default/files/inline/images/19_279.jpg https://gas-kvas.com/uploads/posts/2023-03/1678236833_gas-kvas-com-p-krasivie-realistichnie-risunki-zhivotnikh-3.jpg
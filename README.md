# VK scraper

This python script can be used for saving text posts from VK wall

To use it perform these steps:

1. Open https://vkhost.github.io/ and obtain `access_token`
2. Enter `python3 -m pip install vk_api`
3. Launch the script with `python3 main.py`
4. Enter your phone number, `access_token` and `id` of required resource (like `id12345` or `club12345`, not the full address)

If done right the script will produce output into `dumps` folder. For each scraped resource files `resourse_dump.json` and `resource_posts.txt` will be generated. The first contains all data from the wall, the second one contains only numerated text posts

Resulting files will have different names for different resources, so you can use it multiple times if you need it

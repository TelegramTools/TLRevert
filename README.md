<p align="center">
  <img src="https://github.com/TelegramTools/TLRevert/raw/master/images/Intro.png">
</p>

# TLRevert

This application will remove all the messages that were created by other Telegram Tools, leaving everything as if nothing has happened.

Currrently, the only tools that create messages in chats are **TLMerger** and **TLImporter**

## How does it work?

Each Telegram Tools (currently, **TLImporter** and **TLMerger**) program that creates messages inside a Telegram chat will create a database that stores all the details
of the operations performed and the messages that have been sent. Using that database, TLRevert will find and delete
the messages.

## Download

You can always grab the latest version heading over the [releases tab](https://github.com/TelegramTools/TLRevert/releases).
I built binaries for **Windows (64 bits)**, **Linux amd64** and **Linux armhf**

* On **Windows**: Simply double click on the ``.exe`` file
* On **Linux**: Download the binary, ``cd`` to the folder where the download is located and do ``chmod +x TLRevert-xxx && ./TLRevert-xxx``

If you're running other systems (like MacOS), you will need to **build the files from source**.

## Build from sources

Make sure that you replace the ``api_id`` and ``api_hash`` variables in the ``TLRevert.py`` file.
Read instructions [here](https://core.telegram.org/api/obtaining_api_id) for getting your own from Telegram.

# Credits

Huge thanks to [Telethon](https://github.com/LonamiWebs/Telethon), and his great creator, [Lonami](https://github.com/Lonami), who always was up to answering questions and helping in development. I'm so grateful for his patience :).
Thanks to the [PyInstaller](https://www.pyinstaller.org/) team for their great tool, which I used to build the binaries.

Also, huge acknowledgements to Telegram for making such a great messenger!

**Give always credits to all the original authors and owners when using some parts of their hard work in your own projects**

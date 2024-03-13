# P2PCam

Intended to use/view a camera from an external computers camera

## Contents

1. [Introduction](#introduction)

2. [Usage](#usage)

3. [Credits](#credits)

4. [License](#license)

5. [Disclaimers](#disclaimers)

---

## Introduction

The purpose and focus of this project is to provide an open source, easy to use, and minimalist solution to having no webcam on a computer, but having a laptop webcam available externally.

This project uses a server/client system, where the server is sending the video data to a client, as soon as it connects to it via a socket. The client then displays it within a Windows desktop application.

## Usage

1. Clone the repository on a computer with a webcam, eg. a laptop, and the client without a webcam. [Click here to download the repository as a zip file.](https://github.com/EEkebin/P2PCam/archive/refs/heads/main.zip)

    ```sh
    git clone https://github.com/EEkebin/P2PCam
    ```

2. Navigate to the directory.

    ```sh
    cd ./P2PCam/
    ```

3. Install the required dependent python packages, given in `requirements.txt`.

    ```sh
    pip install -r ./requirements.txt
    ```

4. Check IP Address of computer with a webcam.

    ```sh
    ipconfig
    ```

5. In `client.py`, change host_ip to the IP Address of the computer with a webcam.

6. If you need a different port to use, change it to such in both `server.py` and `client.py`.

7. Run the `server.py` on the computer with a webcam.

    ```sh
    python ./server.py
    ```

8. Run the `client.py` on the computer without a webcam.

    ```sh
    python ./client.py
    ```

9. Use Open Broadcaster Software (OBS) to start a Virtual Camera with a Window Capture to capture the window that is displaying the webcam playback.

10. Success.

## Credits

> [EEkebin](https://github.com/EEkebin)

## License

> [P2PCam is licensed under the GNU General Public License v3.0.](https://github.com/EEkebin/P2PCam/blob/main/LICENSE)

## Disclaimers

> This project, P2PCam, and/or its contributors are not sponsored by or affiliated with any of the packages or technologies used in this project.

> This project, P2PCam, and/or its contributors are not sponsored by or affiliated with Open Broadcaster Software (OBS) or any of its affiliates.

> This project, P2PCam, and/or its contributors are not responsible for the actions of end users. All liabilities and responsibilities lie with the end user for the misuse(s) of P2PCam and/or any other products and/or services.

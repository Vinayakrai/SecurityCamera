# SecurityCamera

**SecurityCamera** is a Python-based application that utilizes OpenCV and the `winsound` module to detect human motion through a webcam. Upon detecting motion, it emits a beep sound to alert the user.

## 🚀 Features

- **Motion Detection**: Continuously monitors the webcam feed to detect human movement.
- **Audio Alert**: Emits a beep sound when motion is detected.
- **Real-time Processing**: Processes video feed in real-time for immediate detection.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **OpenCV**: For image processing and motion detection.
- **winsound**: For audio alerts (Note: `winsound` is available only on Windows platforms).

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/SecurityCamera.git
cd SecurityCamera
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install opencv-python
```

## 🚀 Usage

Run the script using Python:

```bash
python securitycamera.py
```

The script will:

1. Access your system's default webcam.
2. Continuously monitor for motion.
3. Emit a beep sound when motion is detected.

## ⚠️ Notes

- The `winsound` module is specific to Windows. If you're using a different operating system, you'll need to replace the audio alert functionality with an alternative method compatible with your OS.
- Ensure your webcam is properly connected and accessible by the system.

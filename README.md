# Right Hand Finger Instrument

A TouchDesigner component that reads the position of your right hand and fingers to play an instrument. The component allows you to play notes in a 7th chord based on your finger positions.

## Features

- **Right Hand Tracking**: Uses the camera to track the position of your right hand and fingers.
- **Finger-to-Note Mapping**: Each finger from the index to pinky corresponds to a note in a 7th chord.
- **Dynamic Note Generation**: The note played is determined by the horizontal position of your index finger.
- **7th Chord Structure**: The chord is based on the index finger's position, with each finger playing a note in the chord.

## How It Works

The component uses the position of your right hand and fingers, particularly focusing on the horizontal position of the index finger, to determine the root note of the chord. The subsequent fingers (middle, ring, pinky) are mapped to notes in a 7th chord, with each finger press corresponding to a note.

## Setup Instructions

1. Clone or download this repository.
2. Drag the .tox file into your Touch Designer Project.
3. Connect a TOP input to the component.
4. Connect a VST through the VST chop inside the component.
5. Connect the audio out output to your audio device output, or use however you want to.

## Requirements

- **TouchDesigner**: Ensure you have TouchDesigner installed (version X.X or higher).
- **Camera**: A webcam to track hand and finger movements.
- **SpoutCam**: Allows you to create a virtual video input device that the component uses (https://spout.zeal.co/).

## Usage

Once set up, move your right hand and position your fingers. The component will automatically start tracking the finger positions and play corresponding notes based on the index finger’s position in the camera.

## Example

Here’s a basic visual demonstration of how it works:

![Example](https://github.com/user-attachments/assets/da347258-8193-4b0b-ab4d-d2e5fc3d77cb)

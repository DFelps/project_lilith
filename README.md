# Lilith

Lilith is a local AI assistant with voice, personality, memory, TTS and a Live2D avatar integrated with VTube Studio.

The project started as a local conversational AI and evolved into a "virtual presence" MVP:

- text-based conversation
- voice responses (TTS)
- lip sync via custom parameter in VTube Studio
- dynamic states like `thinking`, `speaking` and `idle`
- local LLM powered by Ollama
- memory and response style control

---

## Status

Active development.

Current MVP includes:

- CLI-based chat
- local LLM response generation
- local TTS pipeline
- lip sync integration with VTube Studio API
- avatar state control via hotkeys
- async voice queue (generation + playback)

### Next steps

- microphone and system audio capture
- contextual decision-making (when to speak)
- more social behavior in voice calls
- improved natural timing and expressiveness

---

## Stack

### AI & Reasoning
- Python
- Ollama
- Local language model

### Voice
- Coqui XTTS v2
- sounddevice
- soundfile

### Avatar
- VTube Studio
- Live2D
- VTube Studio WebSocket API

### Internal Architecture
- memory system
- persona handling
- intent routing
- basic safety layer
- response builder
- TTS queue
- custom lip sync system

---

## Project Structure

```text
project_lilith/
├── app/
│   ├── brain/
│   ├── core/
│   ├── llm/
│   ├── memory/
│   ├── ui/
│   ├── utils/
│   ├── vision/
│   └── voice/
├── config/
├── data/
│   ├── audio/
│   │   ├── cache/
│   │   ├── generated/
│   │   └── input/
│   ├── brain/
│   ├── knowledge/
│   ├── memory/
│   │   └── sessions/
│   ├── vision/
│   └── voice/
│       └── reference/
├── scripts/
├── tests/
├── .venv/
└── main.py
```

---

## Description

```txt
Local AI assistant with voice, memory and a Live2D avatar, designed for real-time interaction and virtual presence.
```

---

## Author

Daniel Siqueira

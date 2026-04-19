# Lilith

Lilith é uma assistente local com voz, personalidade, memória, TTS e avatar Live2D integrado ao VTube Studio.

O projeto começou como uma IA conversacional local e evoluiu para um MVP de "presença virtual":
- conversa por texto
- responde com voz
- mexe a boca via parâmetro customizado no VTube Studio
- pode alternar estados como `thinking`, `speaking` e `idle`
- usa modelo local via Ollama
- mantém memória e estilo de resposta

## Status

Projeto em desenvolvimento ativo.

Atualmente o MVP já faz:
- chat por CLI
- geração de resposta com LLM local
- TTS local
- lipsync via VTube Studio API
- hotkeys/estados no avatar
- fila de voz com geração e reprodução assíncronas

Próximos passos:
- captura de microfone e áudio do sistema
- decisão contextual de quando interagir
- comportamento mais social em call
- polimento de naturalidade, timing e expressividade

---

## Stack

### IA e raciocínio
- Python
- Ollama
- modelo local de linguagem

### Voz
- Coqui XTTS v2
- `sounddevice`
- `soundfile`

### Avatar
- VTube Studio
- Live2D
- WebSocket API do VTube Studio

### Estrutura interna
- memória
- persona
- roteamento de intenção
- segurança básica
- builder de resposta
- fila de TTS
- lipsync customizado

---

## Estrutura do projeto

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
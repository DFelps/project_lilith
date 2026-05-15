# Lyra

Lyra é uma IA local com personalidade, memória, voz por F5-TTS e base preparada para um companion animado na área de trabalho.

O projeto começou como uma assistente local e agora está sendo reestruturado como uma presença social para desktop/call:

- conversa por CLI
- respostas com LLM local via Ollama
- voz local com F5-TTS
- fila assíncrona de geração/reprodução de áudio
- lipsync por áudio gerado
- estados visuais como `idle`, `thinking` e `speaking`
- memória simples e controle de estilo

## Status

Projeto experimental em desenvolvimento ativo.

MVP atual:

- chat por terminal
- persona carregada de JSON
- geração de resposta via Ollama
- TTS com F5-TTS
- normalização de texto para voz
- estado local do avatar para futura janela própria na área de trabalho
- reprodução de áudio direta, sem depender de app externo

Próximas fases:

- avatar próprio direto na área de trabalho
- mouth sprites `closed`, `half`, `open`
- estado visual `thinking` direto no overlay
- captura de microfone e áudio do sistema
- decisão contextual de quando interagir sozinha
- respostas rápidas em cache para wake word e reações curtas

## Stack

### IA

- Python
- Ollama
- modelo local, por padrão `llama3.1:8b`

### Voz

- F5-TTS
- sounddevice
- soundfile
- numpy
- torch

### Visual atual

- base para avatar próprio na área de trabalho
- estado visual em `data/avatar/state.json`
- sem dependência de app externo no MVP

### Estrutura interna

- core orchestrator
- persona e estilo
- memória local
- roteamento básico
- safety local simples
- fila de TTS
- lipsync baseado no volume do áudio gerado

## Estrutura

```text
project_lyra/
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
│   ├── brain/
│   ├── knowledge/
│   ├── memory/
│   ├── models/
│   ├── vision/
│   └── voice/
│       └── reference/
├── scripts/
├── tests/
├── main.py
└── requirements.txt
```

## Instalação

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ollama

Deixe o Ollama rodando localmente:

```text
http://127.0.0.1:11434
```

Modelo padrão:

```bash
ollama run llama3.1:8b
```

## F5-TTS

Arquivos esperados:

```text
data/voice/reference/lyra_reference.wav
data/voice/reference/lyra_reference.txt
```

Modelo PT-BR local esperado por padrão:

```text
data/models/f5_ptbr/model_last.safetensors
data/models/f5_ptbr/vocab.txt
```

Esses arquivos são locais e não devem ser versionados se forem pesados ou privados.

Variáveis opcionais:

```text
LYRA_F5_SPEED=0.72
LYRA_F5_NFE_STEP=32
LYRA_F5_CFG_STRENGTH=1.2
LYRA_F5_SWAY=-1
LYRA_F5_CKPT=data/models/f5_ptbr/model_last.safetensors
LYRA_F5_VOCAB=data/models/f5_ptbr/vocab.txt
```

## Avatar desktop

A integração antiga foi removida. A Lyra agora grava o estado visual em `data/avatar/state.json`, que pode ser consumido por uma futura janela própria em Electron/PixiJS.

Estados atuais:

```text
idle
thinking
speaking
```

## Rodando

```powershell
python main.py
```

Exemplo:

```text
Lyra pronta. Digite sua mensagem. Use 'sair' para encerrar.

Você: quem é você?
Lyra: Sou Lyra. Falo com você agora.
```

## Arquivos locais ignorados

O `.gitignore` evita subir:

- `.venv/`
- `tools/`
- modelos pesados
- áudios gerados
- referências de voz privadas
- base local de conhecimento

## Roadmap curto

- [x] CLI local
- [x] persona JSON
- [x] resposta com Ollama
- [x] F5-TTS
- [x] fila de voz
- [x] voz com F5-TTS sem dependência de app externo
- [ ] avatar próprio em PySide6/PyQt
- [ ] sprites de boca: closed, half, open
- [ ] blink automático
- [ ] cache de respostas rápidas
- [ ] captura de microfone
- [ ] captura de áudio do sistema
- [ ] decider para interação autônoma

## Aviso

Lyra é um projeto experimental local. A proposta é prototipar uma presença virtual com voz, memória e comportamento social controlado.

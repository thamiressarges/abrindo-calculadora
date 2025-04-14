# Abrindo Calculadora com PyAutoGUI

Este script automatiza o processo de abrir a Calculadora do Windows utilizando a biblioteca `pyautogui` do Python.

## 💻 Requisitos

Antes de rodar o script, instale a biblioteca necessária com o seguinte comando:

```bash
pip install pyautogui

## 🚀 Como funciona

O script move o mouse, digita "calculadora" e clica pra abrir o app.
---

## 📌 Observações importantes

- As posições do mouse (`x`, `y`) podem variar de acordo com a resolução da tela e o layout do sistema operacional. Você pode usar `pyautogui.position()` para identificar novas posições e ajustar conforme necessário.
- O tempo de espera (`sleep`) entre as ações é importante para garantir que o sistema responda corretamente antes do próximo comando.
- O script foi testado em Windows com a Calculadora padrão.

---

## 🧠 Dica útil

Caso queira identificar novas posições da tela, descomente a linha abaixo e execute o script:

```python
#print(posicaoMouse.position())

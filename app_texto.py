import gradio as gr 

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

iface = gr.Interface(
    fn = reverter_texto,
    title = "Reverter Texto",
    inputs = "text",
    outputs = ["text", "number"],
    description = "Insira um texto para revertê-lo e contar os caracteres "
)

iface.launch(share=True)
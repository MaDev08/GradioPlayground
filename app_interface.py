import gradio as gr 

# Para customizar as aplicações gradio é exigido um pouco de HTML e CSS
def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    estilo = (
        f"color: {cor_texto};",
        f"background-color: {cor_fundo};",
        f"font-size: {tamanho_fonte};",
        f"font-family: {estilo_fonte};",
    )
    return f'<div style="{estilo}">{texto}</div>'

iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite seu texto aqui..."),
        gr.ColorPicker(label="Cor do Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho da Fonte", value=20 ),
        gr.Radio(
            choices = ["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
            label = "Estilo da Fonte"
        ),
    ],
    outputs= gr.HTML(label = "Texto Customizado"),
    title = "Customizador de Texto",
    description = "Customize o seu texto com cor, tamanho e estilo da fonte"
)

iface.launch(share=True)
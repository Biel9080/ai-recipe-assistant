# ============================================
# INSTALAÇÃO DAS BIBLIOTECAS
# ============================================
!pip install -q langchain langchain-community langchain-groq

# ============================================
# IMPORTAÇÕES
# ============================================
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# ============================================
# CONFIGURAÇÕES (COLOQUE SUA CHAVE AQUI)
# ============================================
os.environ["GROQ_API_KEY"] = "SUA_CHAVE_AQUI"  # Substitua pela sua chave

# ============================================
# MODELO DE IA (GROQ)
# ============================================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7  # maior criatividade
)

# ============================================
# PROMPT (GERADOR DE RECEITAS)
# ============================================
prompt = ChatPromptTemplate.from_template("""
PAPEL:
Você é um chef especialista em receitas culinárias.

OBJETIVO:
Criar receitas completas com base no pedido do usuário.

REGRAS:
- Gere uma receita completa (ingredientes + modo de preparo)
- Seja claro, simples e prático
- Organize em etapas
- Inclua tempo de preparo e rendimento
- Não invente ingredientes impossíveis
- Sempre responda em português

PEDIDO DO USUÁRIO:
{pergunta}
""")

# ============================================
# LOOP DE INTERAÇÃO
# ============================================
print("Gerador de Receitas 🍳 (digite 'x' para sair)\n")

chain = prompt | llm

while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() == "x":
        print("Encerrando...")
        break
    
    resposta = chain.invoke({
        "pergunta": pergunta
    })
    
    print("\nReceita:\n", resposta.content, "\n")




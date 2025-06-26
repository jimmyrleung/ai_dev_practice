# Prompt Engineering - Abordagens

```
Como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada?
```
Essa pergunta pode ser enviada diretamente a LLM, conforme a abordagem `zero-shot` prompting, pois é uma pergunta objetiva sobre algo.

---

```
Como fazer a decomposição numérica de 142.981?
```
Essa é uma pergunta um pouco mais vaga, que pode se beneficiar da abordagem `chain-of-thoughts`.
- Exemplo de Prompt: "Passo a passo, descreva como fazer a decomposição númerica de 142.981"

---

```
Quais personagens de 'As Crônicas de Gelo e Fogo' possuem características inspiradas na filosofia de Maquiavel?
```
Essa é uma pergunta que compensa utilizarmos a abordagem `CIDI (context, instructions, details e input)` para que a LLM faça uma análise complexa mais elaborada das personagens com base na filosofia indicada.

```
Exemplo de prompt

Contexto: Atue como um especialista em literatura e filosofia, especialmente na obra "As Crônicas de Gelo e Fogo" e no filósofo Maquiavel

Instruções: Identifique quais personagens dessa obra possuem características associadas a filosofia de Maquiavel

Detalhes: Considere epsecialmente os aspectos comportamentais das personagens e suas respectivas tomadas de decisão

Input: Quais personagens de As Crônicas de Gelo e Fogo possuem características inspiradas na filosofia de Maquiavel.
```

---

Queremos validar o uso de Python e FastAPI para determinados casos de uso, e para isso iremos utilizar uma LLM para nos guiar no seguinte processo:

Criar um endpoint que valide e processe a entrada de um objeto do tipo `Item`, seguindo as especificações abaixo:
1. Estrutura do `Item`:
    1. **nome**: `string` com tamanho máximo de 25 caracteres.
    2. **valor**: `float`
    3. **data**: valor do tipo *date*, que não pode ser superior à data atual.
2. Requisitos
    1. O endpoint deve validar os valores recebidos.
    2. Após a validação, o corpo da requisição(`Item`) deve ser retornado com um novo campo adicional: `uuid`. Este campo deve conter um identificador único gerado dinamicamente.

Essa também é uma situação que compensa utilizar a abordagem `CIDI (context, instructions, details e input)` por ser uma situação mais ampla, que requer determinadas habilidades específicas e um passo a passo mais estruturado.

```
Exemplo de prompt

Contexto: Atue como um Senior Software Engineer especialista na linguagem Python, com vasta experiência em construção de web APIs.

Instruções: Gere um scaffold completo de uma aplicação utilizando FastAPI com um endpoint de validação seguindo boas práticas. Esse endpoint será responsável por validar um objeto do tipo `Item`, e caso esteja válido, o mesmo deve ser retornado na resposta com um campo adicional `uuid` único gerado dinamicamente.

Detalhes: Um objeto válido do tipo `Item` tem as seguintes propriedades: 
- nome: `string` com tamanho máximo de 25 caracteres.
- valor: `float`
- data: `date` e não pode ser superior à data atual.
```
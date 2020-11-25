# Pyliwcbr (em desenvolvimento)

Pyliwcbr é uma biblioteca de acesso ao dicionário pyliwcbr.

## 🦾Uso 

```python
import pyliwc.Liwc

liwc = Liwc("path/to/dict/file.dic)

```

## 📄Modelos

- Word
- Category
- Sentence
- Liwc

---
### **Word** 

Classe de palavra que é responsável por referenciar cada palavra do dicionário Liwc.

Um objeto do tipo **Word** possui os seguintes métodos: 

| Método  |  Descrição |
| ------- |-----|
| ```get_categories() ``` | Listar todas as categorias que a palavra foi classificada |
|```get_value() ``` | Pegar o valor textual da palavra |
|```get_categories_ids() ``` | Pegar listar o id de todas as categorias que a palavra foi classificada. |


---
### **Category** 

Classe de categoria que é responsável por referenciar cada categoria do dicionário Liwc.

Um objeto do tipo **Category** possui os seguintes métodos: 

| Método  |  Descrição |
| ------- |-----|
| ```get_id() ``` | Pegar o **id** númerico da categoria |
|```get_tag() ``` | Pegar o valor textual da categoria |
|```get_words() ``` | Listar todas as palavras que possui o objeto como categoria. |
|```get_parent_category() ``` | Pegar a categoria pai da categoria. (*em desenvolvimento*) |


### **Sentence** 

Classe de sentença que é responsável por referenciar uma sentença. Classe utilizada como objeto de retorno ao informar uma mensagem para se analisar ao objeto liwc.

O objeto **Sentence** possui os seguintes métodos: 



### **Liwc** 

Classe de controle ao dicionário liwc, responsável por informar os principais itens de processamento. Além disso, responsável por processar as funcionalidades principais de processar frases


O objeto **Liwc** possui os seguintes métodos: 





## License
[MIT](https://choosealicense.com/licenses/mit/)
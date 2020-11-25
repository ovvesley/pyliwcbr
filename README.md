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

Classe de sentença é responsável por referenciar uma sentença. Classe utilizada como objeto de retorno ao informar uma mensagem para analisar no objeto liwc.

O objeto **Sentence** possui os seguintes métodos: 

| Método  |  Descrição |
| ------- |-----|
| ```get_words() ``` | Pegar todos as instancias de Word dentro da sentença  |
|```get_categories() ``` |Pegar todos as instancias de Category dentro da sentença |
|```get_raw_value() ``` | Pegar o valor da sentença.(*em desenvolvimento*) |

### **Liwc** 

Classe de controle ao dicionário liwc, responsável por informar os principais itens de processamento. Além disso, responsável por processar as funcionalidades principais de processar frases


O objeto **Liwc** possui os seguintes métodos: 

| Método  |  Descrição |
| ------- |-----|
| ```get_words() ``` | Pegar todas as palavras do dicionario; cada separada em instancia da classe Word|
|```get_categories() ``` |Pegar todas as categorias do dicionario; cada separada em instancia da classe Category |
|```find_id_category(identifier) ``` | Buscar uma categoria através do Id da categoria|
|```raw_word_equals_word_obj(raw_word, word) ``` | Verificar igualdade entre string de palavra e objeto instancia de Word|
|```find_word_by_raw_word(str_word) ``` | Buscar instancia de Word que possui str_word como valor.|
|```proccess_sentences(sentence) ``` |Informar uma sentença em string e receber uma instancia de Sentece.|








## License
[MIT](https://choosealicense.com/licenses/mit/)
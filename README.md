# 🔥 Conversor de Unidades - API FastAPI

Este projeto é uma **API de conversão de unidades** desenvolvida com **FastAPI**.  
Ela realiza conversões entre diferentes unidades físicas, conversão de temperaturas e conversão de termopares dos tipos mais utilizados na indústria (K, J e T).

---

## 📦 Funcionalidades

- Conversão de unidades físicas (pressão, volume, comprimento, etc.) usando [Pint](https://pint.readthedocs.io/).
- Conversão de temperatura entre Celsius, Fahrenheit e Kelvin.
- Conversão de termopares dos tipos **K**, **J** e **T**:
  - Celsius para miliVolts (mV)
  - MiliVolts (mV) para Celsius
- Documentação automática no **Swagger UI**.

---

## 🛠️ Tecnologias utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pint](https://pint.readthedocs.io/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- [Pydantic](https://docs.pydantic.dev/)
- [Python 3.11+](https://www.python.org/)

---

## 📁 Estrutura do Projeto

```
Back_end_unit_converter/
├── app/
│   ├── main.py               # Inicia o FastAPI e inclui as rotas
│   ├── routes/
│   │   └── converter_route.py # Define as rotas da API
│   ├── services/
│   │   ├── unit_converter.py      # Conversão de unidades (Pint)
│   │   ├── temperature_converter.py # Conversão de temperaturas
│   │   └── thermocouple_converter.py # Conversão de termopares
│   └── __init__.py
└── README.md
```

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Back_end_unit_converter.git
cd Back_end_unit_converter
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

- Windows:
  ```bash
  .\venv\Scripts\activate
  ```

- Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o servidor

```bash
uvicorn app.main:app --reload
```

Acesse a API em:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Exemplos de uso

### 🔹 Conversão de unidades físicas (`/convert`)

**POST** `/convert`

```json
{
  "value": 1,
  "from_unit": "bar",
  "to_unit": "psi"
}
```

### 🔹 Conversão de temperatura (`/convert-temperature`)

**POST** `/convert-temperature`

```json
{
  "value": 100,
  "from_unit": "C",
  "to_unit": "F"
}
```

### 🔹 Conversão de termopares (`/convert-thermocouple`)

**POST** `/convert-thermocouple`

```json
{
  "value": 25,
  "thermocouple_type": "K",
  "direction": "celsius_para_mv"
}
```

---

## 📚 Referências

- [Tabela de conversão de unidades de pressão](#)
- [NIST ITS-90 Thermocouple Database](https://srdata.nist.gov/its90/main/)

---

## 📃 Licença

Este projeto é livre para uso educacional e não possui licença comercial ativa.

---

## 👌 Autor

Desenvolvido por **Bruno Leonardo Ramos dos Santos**.  
Engenheiro de Instrumentação, Automação e Software.

---


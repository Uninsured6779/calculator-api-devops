# Calculator API, projekt DevOps

## Opis projektu

Projekt stworzyłem jako część zaliczenia przedmiotu DevOps. 

Celem było stworzenie prostej aplikacji webowej oraz opracowanie pełnego procesu automatycznego budowania, testowania i wdrażania aplikacji do chmury AWS z użyciem narzędzi poznanych podczas zajęć.

Wybrałem prosty kalkulator, który udostępnia REST API oraz prosty interfejs webowy, dostępny z poziomu przeglądarki.

---

## Funkcjonalności

Aplikacja udostępnia następujące endpointy:

### GET /health

Endpoint służy do sprawdzania stanu aplikacji.

Przykładowa odpowiedź:

```json
{
  "status": "UP"
}
```

### GET /version

Zwraca aktualnie wdrożoną wersję aplikacji.

Przykładowa odpowiedź:

```json
{
  "version": "1.0.4"
}
```

### POST /calculate

To główny endpoint aplikacji.

Pozwala na wykonywanie podstawowych działań matematycznych:

* dodawanie,
* odejmowanie,
* mnożenie,
* dzielenie.

Przykładowe żądanie:

```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}
```

Przykładowa odpowiedź:

```json
{
  "result": 15
}
```

---

## Architektura rozwiązania

Podczas realizacji projektu użyłem następującego procesu wdrażania:

```text
GitHub
   ↓
GitHub Actions
   ↓
Testy automatyczne
   ↓
Budowa obrazu Docker
   ↓
Docker Hub
   ↓
AWS ECS Fargate
   ↓
Application Load Balancer
   ↓
Publiczny adres URL
```

---

## Wykorzystane technologie

W projekcie wykorzystano:

* Python 3.12
* FastAPI
* Uvicorn
* Pytest
* Docker
* GitHub Actions
* Docker Hub
* AWS ECS Fargate
* AWS Application Load Balancer (ALB)
* AWS CloudWatch
* Terraform

---

## CI/CD

Proces CI/CD zrealizowano z użyciem GitHub Actions.

Po wykonaniu push do gałęzi `main`, automatycznie uruchamia się pipeline, który:

1. pobiera kod z repozytorium,
2. instaluje zależności,
3. uruchamia testy,
4. buduje obraz Docker,
5. publikuje obraz w Docker Hub,
6. wdraża nową wersję aplikacji na AWS ECS.

Dzięki temu, wdrożenie nowej wersji aplikacji odbywa się bez manualnych operacji na serwerze.

---

## Infrastructure as Code

Do konfiguracji infrastruktury wykorzystano Terraform.

Kod Terraform znajduje się w katalogu:

```text
terraform/
```

Terraform zarządza zasobami AWS wykorzystywanymi przez projekt, w tym:

* CloudWatch Log Group,
* Security Group.

Podstawowe polecenia:

```bash
terraform init
terraform plan
terraform apply
```

---

## Uruchomienie lokalne

### Klonowanie repozytorium

```bash
git clone https://github.com/Uninsured6779/calculator-api-devops.git
cd calculator-api-devops
```

### Budowanie obrazu 

```bash
docker build -t calculator-api .
```

### Uruchomienie kontenera 

```bash
docker run -p 8000:8000 calculator-api
```

Po uruchomieniu aplikacja będzie dostępna pod adresem:

```text
http://localhost:8000
```

Dokumentacja Swagger:

```text
http://localhost:8000/docs
```

---

## Docker Hub

Obraz aplikacji znajduje się w repozytorium Docker Hub:

```text
https://hub.docker.com/r/civoh42/calculator-api
```

---

## Publiczny adres aplikacji

Aplikacja została wdrożona na AWS ECS. Został również wykorzystany AWS ALB, aby aplikacja miała stały adres publiczny, który podano poniżej:

```text
http://calculator-alb-1051564374.eu-central-1.elb.amazonaws.com/
```

Przykładowe endpointy:

```text
http://calculator-alb-1051564374.eu-central-1.elb.amazonaws.com/health
http://calculator-alb-1051564374.eu-central-1.elb.amazonaws.com/version
http://calculator-alb-1051564374.eu-central-1.elb.amazonaws.com/docs
```

---

## Logowanie i monitoring

Logi aplikacji są dostępne w usłudze AWS CloudWatch.

W projekcie wykorzystano również endpoint `/health`, który pozwala sprawdzić poprawne działanie aplikacji.

---

## Repozytorium

Kod źródłowy projektu:

```text
https://github.com/Uninsured6779/calculator-api-devops
```

---

## Podsumowanie

W ramach projektu zrealizowano następujące elementy:

* aplikacja webowa z endpointami `/health`, `/version` oraz `/calculate`,
* konteneryzacja przy użyciu Dockera,
* automatyczne testy,
* pipeline CI/CD w GitHub Actions,
* wdrożenie aplikacji na AWS ECS,
* publiczny adres URL,
* Infrastructure as Code z użyciem Terraform,
* logowanie aplikacji w AWS CloudWatch.

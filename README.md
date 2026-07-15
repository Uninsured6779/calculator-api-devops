# Calculator API – projekt DevOps

## Opis projektu

Projekt stworzyłem jako część zaliczenia przedmiotu DevOps.

Celem było przygotowanie prostej aplikacji webowej oraz opracowanie pełnego procesu automatycznego budowania, testowania i wdrażania aplikacji do chmury AWS z wykorzystaniem narzędzi poznanych podczas zajęć.

Wybrałem prosty kalkulator, który udostępnia REST API oraz podstawowy interfejs webowy dostępny z poziomu przeglądarki.

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
  "version": "1.0.8"
}
```

### POST /calculate

Jest to główny endpoint aplikacji.

Pozwala wykonywać podstawowe działania matematyczne:

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

Podczas realizacji projektu wykorzystałem następujący proces wdrażania:

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

W projekcie wykorzystałem:

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

Proces CI/CD został zrealizowany z wykorzystaniem GitHub Actions.

Po wykonaniu pushu do gałęzi `main` automatycznie uruchamia się pipeline, który:

1. pobiera kod z repozytorium,
2. instaluje zależności,
3. uruchamia testy automatyczne,
4. buduje obraz Docker,
5. publikuje obraz w Docker Hub,
6. wymusza wdrożenie nowej wersji aplikacji w usłudze AWS ECS.

Dzięki temu wdrożenie nowej wersji aplikacji odbywa się bez ręcznego aktualizowania kontenera w AWS.

---

## Infrastructure as Code

Do częściowej konfiguracji infrastruktury wykorzystałem Terraform.

Kod Terraform znajduje się w katalogu:

```text
terraform/
```

Obecna konfiguracja Terraform obejmuje następujące zasoby AWS:

* CloudWatch Log Group,
* Security Group.

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

Dokumentacja Swagger będzie dostępna pod adresem:

```text
http://localhost:8000/docs
```

### Uruchomienie testów

Testy można uruchomić lokalnie poleceniem:

```bash
pytest
```

---

## Docker Hub

Obraz aplikacji znajduje się w repozytorium Docker Hub:

```text
https://hub.docker.com/r/civoh42/calculator-api
```

Gotowy obraz można pobrać i uruchomić poleceniami:

```bash
docker pull civoh42/calculator-api:latest
docker run -p 8000:8000 civoh42/calculator-api:latest
```

---

## Publiczny adres aplikacji

Aplikacja została wdrożona w usłudze AWS ECS Fargate. Ruch do aplikacji jest obsługiwany przez AWS Application Load Balancer, dzięki czemu jest ona dostępna pod jednym publicznym adresem URL:

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

Logi aplikacji są przesyłane do usługi AWS CloudWatch i można je przeglądać z poziomu usługi Amazon ECS.

Endpoint `/health` jest również wykorzystywany przez Application Load Balancer do sprawdzania, czy uruchomiona aplikacja działa poprawnie.

---

## Repozytorium

Kod źródłowy projektu znajduje się pod adresem:

```text
https://github.com/Uninsured6779/calculator-api-devops
```

---

## Podsumowanie

W ramach projektu zrealizowałem następujące elementy:

* aplikację webową z endpointami `/health`, `/version` oraz `/calculate`,
* prosty interfejs użytkownika dostępny w przeglądarce,
* konteneryzację aplikacji przy użyciu Dockera,
* testy automatyczne z wykorzystaniem Pytest,
* pipeline CI/CD w GitHub Actions,
* publikowanie obrazu aplikacji w Docker Hub,
* automatyczne wdrażanie aplikacji na AWS ECS Fargate,
* publiczny adres URL udostępniony przez Application Load Balancer,
* część infrastruktury zarządzaną przy użyciu Terraform,
* logowanie aplikacji w AWS CloudWatch.

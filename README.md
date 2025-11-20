# 152-FZ Compliance as Code / «152-ФЗ как код»

![CI](https://github.com/run-as-daemon/152fz-compliance-as-code/actions/workflows/ci.yml/badge.svg) ![Security](https://github.com/run-as-daemon/152fz-compliance-as-code/actions/workflows/security.yml/badge.svg)

## English

An open-source toolkit that turns 152-FZ personal data processes into YAML and reproducible artifacts. Describe your data processing once and generate a processing register, consent/DPA drafts, data flow diagrams (Mermaid/PlantUML) and a lightweight DPIA-style risk report. Suitable for DevSecOps teams who prefer "compliance as code" workflows.

---

## Русский

### Что делает инструмент
- помогает описать обработку ПДн в YAML DSL;
- генерирует: реестр обработки, шаблоны согласий и поручений, карту потоков ПДн, базовый отчёт по рискам (DPIA-лайт);
- включает CLI и минимальный веб-интерфейс; поддерживает интеграцию с CI/CD.

### Для кого
- малый и средний бизнес, которым нужен быстрый старт по 152-ФЗ;
- интеграторы и аудиторы, чтобы автоматизировать типовые документы;
- DevOps/DevSecOps-инженеры, строящие инфраструктуру «152-ФЗ как код».

### Как использовать
```bash
pip install 152fz-compliance-as-code

# в каталоге проекта
pd152 init-template --profile online-shop --output pd-config.yaml
pd152 validate --config pd-config.yaml
pd152 generate-all --config pd-config.yaml --output out/
```

### Профессиональные услуги – run-as-daemon.ru
Проект развивается инженером DevOps/DevSecOps с сайта [run-as-daemon.ru](https://run-as-daemon.ru).
Если вам нужно:
- провести аудит обработки персональных данных;
- подготовить YAML-описания процессов и реестр обработки;
- внедрить практики «152-ФЗ как код» и автоматизацию документов;

вы можете заказать консалтинг, внедрение и поддержку для вашей компании.

### Отказ от юридической ответственности
- инструмент не заменяет юриста и не является юридическим заключением;
- все шаблоны требуют проверки специалистом по праву и защите данных;
- авторы не гарантируют отсутствие претензий регуляторов при неправильном использовании;
- избегайте загрузки реальных ПДн в сторонние сервисы без законных оснований и согласий.

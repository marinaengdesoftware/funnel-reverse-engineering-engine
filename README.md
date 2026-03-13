# Funnel Reverse Engineering Engine

Sistema experimental para análise automática da arquitetura tecnológica de páginas de vendas.

O objetivo é identificar ferramentas utilizadas em funis de marketing digital, como:

- CMS
- plataformas de vídeo
- pixels de rastreamento
- ferramentas de automação
- plataformas de checkout

A análise é realizada a partir de uma URL e gera um relatório técnico com os componentes detectados.

---

## Arquitetura do sistema
URL
↓
Crawler
↓
HTML Extraction
↓
Technology Detection
↓
Report Generation

---

## Estrutura do projeto
---

detectors/
scripts responsáveis por identificar tecnologias utilizadas na página

crawler/
responsável por baixar o HTML da página

report/
geração de relatórios

scanner/
script principal que executa o sistema

---

## Exemplo de uso


python scanner/scanner.py


Entrada:


https://site.com


Saída:


CMS: WordPress
Video Platform: Vimeo
Facebook Pixel: Detected
Google Analytics: Detected
Checkout: Hotmart


---

## Objetivo do projeto

Este projeto faz parte de uma pesquisa sobre engenharia reversa de sistemas de marketing digital e análise estrutural de funis de vendas.

O objetivo é compreender quais tecnologias e estruturas são utilizadas em funis digitais de alta conversão.

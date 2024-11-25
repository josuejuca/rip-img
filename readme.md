### O que o script faz:
1. **Criação da pasta `rip`:** A pasta será criada no mesmo diretório onde o script é executado.
2. **Redimensionamento inteligente:**
   - Salva as imagens em um formato compactado (`JPEG` ou mantém `PNG` se for o formato original).
   - Ajusta a qualidade gradualmente até atingir o tamanho máximo de 2 MB.
3. **Preserva a maior qualidade possível:** A qualidade começa em 95 e reduz gradualmente, mantendo o equilíbrio entre qualidade e compressão.

---

### Como usar:
1. Coloque o script no mesmo diretório onde estão as imagens.
2. Execute o script:
   ```bash
   python reduzir_imagens.py
   ```
3. As imagens compactadas serão salvas na pasta `rip`.

---

### Observação:
- Certifique-se de ter a biblioteca Pillow instalada:
  ```bash
  pip install pillow
  ```
- Se precisar ajustar o tamanho máximo ou o formato, basta alterar os parâmetros no script.

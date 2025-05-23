# 📑 Dicionário de Dados — Shapefile de Avisos (TerraBrasilis / INPE)

| Nome da Coluna | Descrição |
|----------------|------------|
| **fid** | Código de identificação do aviso, seguido de dígito verificador. Indica se pertence à tabela corrente (`_curr`) ou histórica (`_hist`). |
| **classname** | Classe do aviso. Valores possíveis:<br>🔸 **Degradação:** `'CICATRIZ_DE_QUEIMADA'`, `'CS_DESORDENADO'`, `'CS_GEOMETRICO'`, `'DEGRADACAO'`<br>🔸 **Desmatamento:** `'DESMATAMENTO_CR'`, `'DESMATAMENTO_VEG'`, `'MINERACAO'` |
| **quadrant** | (Fora de uso atualmente). No passado indicava o quadrante nas imagens AWFI. |
| **path_row** | Path e Row (órbita e ponto) das imagens usadas na identificação do aviso. |
| **view_date** | Data da imagem utilizada na detecção do aviso. |
| **sensor** | Nome do sensor que capturou a imagem. |
| **satellite** | Nome do satélite que capturou a imagem. |
| **areauckm** | Área do aviso (ou parte dele) dentro de uma Unidade de Conservação, em quilômetros quadrados. |
| **uc** | Nome da Unidade de Conservação interceptada pelo aviso. |
| **areamunkm** | 🔥 Área do aviso (ou parte dele) dentro de um município, em km². **➡️ Esta é a coluna recomendada para somatórios de área.** |
| **municipali** | Nome do município interceptado pelo aviso. |
| **geocodibge** | Código do município segundo o IBGE (7 dígitos). |
| **uf** | Unidade da Federação (sigla do estado) onde o aviso está localizado. |
| **areatotkm** | Área total do aviso **antes da divisão por intersecção**. ⚠️ **Não usar para soma de áreas.** Útil apenas para filtros por tamanho. |
| **publish_m** | Indicador temporal mensal, usado para configuração em servidores geoespaciais (GeoServer). **Não está presente no shapefile de download.** |
| **geometry** | Geometria espacial do aviso (polígono). |

## 🚩 Observações importantes:
- A coluna **`areamunkm`** é a que deve ser usada para somatórios confiáveis de área, especialmente para análises por município ou estado.
- As colunas espaciais (`geometry`) podem ser usadas para operações de intersecção, área, centroide, entre outras.
- As colunas textuais como **`uc`** (unidade de conservação) e **`municipali`** ajudam na espacialização dos dados em análises geográficas.

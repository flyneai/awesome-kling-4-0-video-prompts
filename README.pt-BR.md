<div align="center">

![Flyne AI Kling 4.0 prompt library](assets/images/flyne-kling-cover.png)

# Awesome Kling 4.0 Prompts — Guia em português

52 prompts originais e prontos para produção em cinema, publicidade, UGC, diálogo, VFX, animação, gastronomia, viagem, educação e redes sociais.

[English](README.md) · [Español](README.es-ES.md) · **Português (Brasil)** · [15 idiomas](docs/LANGUAGES.md)

[Catálogo](prompts/README.md) · [Método completo](docs/PROMPT-GUIDE.md) · [Áudio multilíngue](docs/MULTILINGUAL-AUDIO.md) · [Flyne AI](docs/FLYNE.md)

</div>

<!-- brand-intro:start -->
[Criar com Flyne AI](https://flyne.ai/model/kling-4-0/) · [Vídeos do X e exercícios originais](docs/X-VIDEOS.md) · [4 exercícios](prompts/inherited-flash-exercises.md)

**Kling 4.0 Flash já está disponível no [site oficial](https://kling.ai/) em acesso antecipado para assinantes anuais Ultra. A [Flyne AI](https://flyne.ai/model/kling-4-0/) prevê oferecer suporte em outubro de 2026; a data exata será anunciada depois.** Em 30 de setembro, o modelo selecionado na Flyne é Kling 3.0 Turbo. Confira antes de gerar.
<!-- brand-intro:end -->


> **Status do modelo — 29/09/2026:** Kling 4.0 Flash entrou em acesso antecipado em 28 de setembro para assinantes do plano Ultra anual. Segundo o [anúncio oficial da Kling AI](https://sg.linkedin.com/company/kling-ai-api), o Kling 4.0 completo e o acesso à API estão previstos para outubro de 2026, sem data exata. A geração nativa de até **30 segundos** foi anunciada para o modelo completo; esse limite ainda não está confirmado para o Flash. Os prompts atuais têm 5–15 segundos.

## Kling 4.0: novidades e disponibilidade

Segundo o [anúncio oficial da Kling AI no X](https://x.com/Kling_ai/status/2104596718067257458), o Flash está em acesso antecipado para assinantes Ultra anuais; o 4.0 completo e a API estão previstos para outubro de 2026. Para o modelo completo foram anunciados até 30 segundos por geração, 10 quadros-chave, 15 referências multimodais, saída de até 4K/10-bit HDR, áudio estéreo e mais idiomas e sotaques. **Esses números não são limites confirmados do Flash.** Os 52 prompts atuais usam cronogramas de 5–15 segundos.

## Vídeos e prompts no X

**Verificado em 29/09/2026.** O [vídeo oficial de apresentação](https://x.com/Kling_ai/status/2104596718067257458) é uma montagem da família 4.0; sua duração total não comprova a duração de uma geração Flash. Os casos abaixo são testes descritos pelos próprios criadores, não benchmarks oficiais nem reproduções independentes deste projeto. Consulte vídeos e textos integrais nos posts originais; não os copiamos.

| Post original | Ideia prática para testar |
|---|---|
| [Umesh: perseguição noturna de um gato, 20 s](https://x.com/umesh_ai/status/2104595267794460949) · [prompt original](https://x.com/umesh_ai/status/2104595270671724936) | Um protagonista, trajeto conectado e um evento físico por local; câmera acompanha sem cortes. |
| [OscarAI: show em anime, 20 s, com prompt](https://x.com/Artedeingenio/status/2104829034299351079) | O criador prefere instruções curtas e diretas nos testes iniciais, mas relata aderência imperfeita. Comece por sujeito → mudança → câmera → final. |
| [とすくん: mudança de clima, 15 s](https://x.com/tokyo_Valentine/status/2104810060811833710) · [prompt original](https://x.com/tokyo_Valentine/status/2104810064750239987) | Use a ficha da personagem só para identidade e roupa; marque separadamente quando clima, luz e atuação mudam. |
| [Alexandra Dekimpe: testes de produção](https://x.com/HadesDesign/status/2104878440889417957) | Descreva microações visíveis em vez de emoções abstratas; fixe causa e efeito com “somente depois”; dê fala exata ou peça silêncio. São observações da autora. |
| [Aswin Aji Raj: UGC em hindi, 20 s](https://x.com/Aswin_Aji_Raj/status/2104867308514779222) | O prompt completo não foi publicado. Defina falante e texto exato; revise pronúncia, sincronia labial e alegações do produto. |
| [@plasm0: comparação 3.0/Flash com mesmo prompt](https://x.com/plasm0/status/2104597949485629557) | Mantenha prompt e referências iguais para um teste A/B e registre as configurações. Um par de vídeos não é benchmark formal. |

**Exercício vertical original de 15 s, ainda não testado** (fora dos 52 prompts do catálogo; sem copiar textos do X):

~~~text
[OBJETO/REFERÊNCIA] Uma única lanterna recarregável de bicicleta, sem marca, com corpo grafite fosco e apenas um botão âmbar. Se houver imagem, ela fixa somente o formato da lanterna.
[CENA/CÂMERA] Oficina de bicicletas tranquila ao entardecer. Plano próximo e contínuo das mãos da mecânica até a lanterna e o guidão. Luz natural da janela; sem cortes ou teletransporte.
[0–4 s] Ela coloca a lanterna apagada ao lado do guidão; mostrar as duas mãos e o suporte.
[4–8 s] Encaixa a lanterna. Só depois do clique que confirma a fixação o polegar aperta o botão âmbar.
[8–12 s] A luz acende apenas uma vez, iluminando a roda dianteira e um pequeno trecho do chão. A câmera desliza de lado para revelar o feixe.
[12–15 s] Ela solta o guidão; a lanterna permanece firme. Sustentar um quadro final estável.
[ÁUDIO/RESTRIÇÕES] Som ambiente da oficina, um clique do encaixe e um do botão; sem fala ou música. Preservar formato, número de mãos, posição e direção da luz. Sem marca, lanternas extras ou cortes sem motivo.
~~~

Teste tanto instruções breves quanto roteiros longos, mas bem estruturados. Registre modo, duração, referências e resultado antes de marcar uma receita como “testada”. Contribuições originais são bem-vindas pelo [guia de contribuição](CONTRIBUTING.md).

## Estrutura rápida

```text
[SAÍDA] duração, proporção, tomada única/múltiplos planos, acabamento
[CONTINUIDADE] características fixas de pessoa, roupa, produto e objetos
[ESPAÇO] local, horário, luz e posições iniciais
[PLANOS POR TEMPO] uma ação principal + uma intenção de câmera por trecho
[ATUAÇÃO E FÍSICA] olhar, respiração, contato, peso e inércia
[ÁUDIO] falante, idioma, tom, ambiente, foley e música
[RESTRIÇÕES] identidade, direção, luz, texto, logotipos e deformações
```

Português é um idioma de documentação deste projeto, mas não está na lista verificada de fala nativa do Kling 3.0. Teste a fala no modelo ativo ou adicione uma locução revisada na pós-produção.

## Destaques

- [Reencontro multilíngue](prompts/cinematic-and-dialogue.md#2-the-paper-crane-at-platform-seven)
- [Anúncio de bebida botânica](prompts/commercial-and-ugc.md#1-botanical-spark-product-reveal)
- [Perseguição de ficção científica](prompts/action-and-vfx.md#1-the-glass-manta-pursuit)
- [Loop cômico do guarda-chuva](prompts/education-documentary-social.md#3-the-infinite-umbrella-problem)

<!-- brand-footer:start -->
<a id="flyne"></a>

## Criar com Flyne AI

**Kling 4.0 Flash já está disponível no [site oficial](https://kling.ai/) em acesso antecipado para assinantes anuais Ultra. A [Flyne AI](https://flyne.ai/model/kling-4-0/) prevê oferecer suporte em outubro de 2026; a data exata será anunciada depois.** Em 30 de setembro, o modelo selecionado na Flyne é Kling 3.0 Turbo. Confira antes de gerar.

[Como usar](docs/FLYNE.md)

## API Kling 4.0 da FLAQ AI · Kling 3.0 Std / Pro

Para integrar geração de vídeo ao seu aplicativo, recomendamos conhecer as APIs Kling da FLAQ AI.

- [Kling 4.0 API · Texto para vídeo](https://flaq.ai/models/kuaishou/kling-4-0-text-to-video/) — Transforme descrições de cenas em vídeos para anúncios, redes sociais e ideias de histórias.
- [Kling 4.0 API · Imagem para vídeo](https://flaq.ai/models/kuaishou/kling-4-0-image-to-video/) — Anime uma imagem de referência com instruções de movimento, para produtos, retratos ou ilustrações.

Verificado em 30/09/2026: as duas páginas indicam **Coming Soon (em breve)**. São páginas de apresentação dos modelos da API; confira disponibilidade, parâmetros e preços quando a integração for lançada.

- [Kling 3.0 Std API](https://flaq.ai/models/kuaishou/kling-3-0-std-text-to-video/) — Texto para vídeo para rascunhos econômicos e variações em lote.
- [Kling 3.0 Pro API](https://flaq.ai/models/kuaishou/kling-3-0-pro-text-to-video/) — Texto para vídeo para projetos que priorizam qualidade visual; compare o mesmo prompt com Std.

[Guia de seleção e integração de API (inglês / chinês)](docs/FLAQ-AI.md)

## Parceria de afiliados

A Flyne AI convida criadores, autores de tutoriais e avaliadores ao [programa de afiliados](https://flyne.ai/affiliate-program/). Hoje, a comissão é de 20% no primeiro pedido pago válido e 10% nos seguintes dentro de 60 dias após o cadastro. Consulte as condições atuais e informe sua relação de afiliado.
<!-- brand-footer:end -->

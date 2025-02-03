# Aula 2: **O que é Criptografia**

## 1. Abertura

Olá! Bem-vindo à aula 2 do curso **Frontend Web3**. Hoje, vamos mergulhar no fascinante mundo da criptografia, uma das bases tecnológicas da Web3 e da blockchain. A criptografia é essencial para garantir segurança, privacidade e confiança em transações digitais.

### Programação:

1. História da criptografia
2. Hash functions
3. Criptografia Simétrica
4. Criptografia Assimétrica

---

## 2. História da Criptografia

A criptografia não é uma invenção recente. Ela existe há milênios, evoluindo de técnicas simples para sistemas complexos que protegem a informação na era digital.

### Marcos importantes:

- **Antiguidade**: Cifras como a **Cifra de César** eram usadas para enviar mensagens secretas em guerras e diplomacia.
- **Segunda Guerra Mundial**: A máquina **Enigma**, usada pelos nazistas, foi um marco na criptografia moderna. Sua quebra por Alan Turing e sua equipe foi crucial para o fim da guerra.
- **Era Digital**: Com o advento da internet, a criptografia se tornou essencial para proteger comunicações e transações online. Algoritmos como **RSA** e **AES** são amplamente utilizados hoje.

### Por que isso importa?

A criptografia é a base da segurança na Web3. Sem ela, não seria possível garantir a autenticidade, integridade e privacidade das transações em blockchains.

---

## 3. Hash Functions

### O que são?

Hash functions são algoritmos que transformam qualquer conjunto de dados (texto, números, arquivos) em uma sequência fixa de caracteres, chamada de **hash**. Esse processo é unidirecional, ou seja, não é possível reverter o hash para obter os dados originais.

### Exemplo de uma hash functions de SHA256

```
INPUT (array de bytes de qualquer tamanho)
            👇
          SHA256
            👇
OUTPUT (array de bytes 256 bits)
```

### Exemplo Real de uma hash functions de SHA256

> [!WARNING]
> Na prática, sempre temos que converter a entrada para bytes e saída precisa ser convertida em hexadecimal

```javascript
sha256("Frontend");
// af48bcf0b9511b39b91b89c70abfbcdc587d3f91b224a24f683d854846ae9c36
sha256("Front-end");
// 32b636e3d6ec560af527cae3dbe9dee7700c49e734868e6482cbfa65a0a1e60b
```

### Características principais:

- **Determinístico**: Os mesmos dados sempre geram o mesmo hash.
- **Rápido**: O cálculo do hash é eficiente, mesmo para grandes volumes de dados.
- **Resistente a colisões**: É extremamente difícil encontrar dois conjuntos de dados diferentes que gerem o mesmo hash.
- **Pequena mudança, grande diferença**: Uma pequena alteração nos dados originais resulta em um hash completamente diferente.

### Exemplos de algoritmos de hash:

- **SHA-256** (usado no Bitcoin)
- **Keccak-256** (usado no Ethereum)
- **BLAKE2b** (alto desempenho e segurança, usado na Polkadot, Solana, Aptos e Sui)

### Aplicações na Web3:

- **Merkle Trees**: Estruturas de dados usadas em blockchains para verificar a integridade de grandes conjuntos de dados.
- **Prova de trabalho (Proof of Work)**: Mineração de criptomoedas usa hash functions para validar transações.
- **Assinaturas digitais**: Hash functions são usadas para garantir a integridade de mensagens e transações.
- **ID de transações e blocos**: Hash functions são usadas para gerar identificadores únicos e imutáveis, garantindo rastreabilidade e segurança.

---

## 4. Criptografia Simétrica

### O que é?

A criptografia simétrica usa uma **única chave** para criptografar e descriptografar dados. A mesma chave é compartilhada entre o remetente e o destinatário.

### Como funciona:

1. O remetente usa a chave para criptografar a mensagem.
2. A mensagem criptografada é enviada ao destinatário.
3. O destinatário usa a mesma chave para descriptografar a mensagem.

### Vantagens:

- **Eficiência**: Algoritmos simétricos são rápidos e consomem menos recursos computacionais.
- **Simplicidade**: Fácil de implementar e usar.

### Desvantagens:

- **Distribuição de chaves**: Compartilhar a chave de forma segura pode ser um desafio.
- **Segurança**: Se a chave for comprometida, toda a comunicação fica vulnerável.

### Exemplos de algoritmos simétricos:

- **AES (Advanced Encryption Standard)**
- **DES (Data Encryption Standard)**
- **3DES (Triple DES)**

### Aplicações na Web3:

- **Armazenamento seguro de dados**: Criptografia de arquivos em sistemas descentralizados como IPFS.
- **Comunicação privada**: Proteção de mensagens em aplicativos descentralizados.
- **Gerenciamento de chaves**: Uso de HSMs (Hardware Security Modules) para armazenamento seguro de chaves criptográficas.

---

## 5. Criptografia Assimétrica

### O que é?

A criptografia assimétrica usa um **par de chaves**: uma chave pública e uma chave privada. A chave pública pode ser compartilhada livremente, enquanto a chave privada deve ser mantida em segredo.

### Posibilidades de uso:

1. Confidencialidade:

- Se alguém quer enviar uma mensagem confidencial para você, ela usam sua chave pública para criptografar a mensagem. Somente você, com sua chave privada, pode descriptografar e ler a mensagem.

2. Autenticação:

- Em Blockchain, a chave privada é usada para gerar uma assinatura digital que comprova a identidade do usuário, assim somente o dono dos ativos pode transferi-lo.

3. Integridade de Dados:

- Quando um documento é assinado digitalmente o destinatário pode usar a chave pública do remetente para verificar a autenticidade e a integridade do documento.

4. Não Repúdio:

- Isso significa que uma vez assinado, o usuário não pode negar ter realizado uma transação.

5. Troca Segura de Chaves (Key Exchange):

- Permiti que duas partes gerem uma chave secreta e compartilhem, mesmo em um canal inseguro usando criptografia assimétrica e simétrica.

### Vantagens:

- **Segurança**: A chave privada nunca é compartilhada, reduzindo o risco de interceptação.
- **Autenticidade**: Permite a criação de assinaturas digitais, garantindo a autenticidade da mensagem.

### Desvantagens:

- **Eficiência**: Algoritmos assimétricos são mais lentos e consomem mais recursos que os simétricos.
- **Complexidade**: Mais difícil de implementar e gerenciar.

### Exemplos de algoritmos assimétricos:

- **RSA (Rivest-Shamir-Adleman)**
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**
- **Ed25519**

### Aplicações na Web3:

- **Assinaturas digitais**: Validação de transações em blockchains.
- **Carteiras digitais**: Chaves públicas e privadas são usadas para gerenciar endereços e assinar transações.
- **Autenticação**: Login em Dapps usando chaves criptográficas.

---

## 6. Conclusão

Por essa aula é isso! Hoje, exploramos a história da criptografia, entendemos o que são hash functions e como elas são usadas para garantir integridade de dados. Além disso, vimos os conceitos de criptografia simétrica e assimétrica, que são fundamentais para a segurança na Web3. Esses conhecimentos são a base para entender como blockchains e outras tecnologias descentralizadas funcionam.

---

## Lição de casa

- Pesquise sobre o algoritmo SHA-256 e escreva um resumo de como ele funciona.
- Experimente gerar hashes de textos usando ferramentas online (por exemplo, [MD5 Hash Generator](https://www.md5hashgenerator.com/)).
- Leia sobre o funcionamento do RSA e como ele é usado em assinaturas digitais.

---

## 7. Próxima aula

Na próxima aula, vamos aprender **O que é uma Wallet**. Nos vemos lá!

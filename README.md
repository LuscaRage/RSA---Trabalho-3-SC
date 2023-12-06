# RSA---Trabalho-3-SC



Esse é o terceiro e último projeto de SC. O trabalho está dividido em 3 partes, sendo elas: Geração de chaves e Cifra (RSA usando OAPC), Assinatura (Cifração com o hash da mensagem) e Verificação (Cálculo e comparação do rash do arquivo). 	 




## Como Rodar
1. Execute esse comando no terminal.
```
python RSA.py
```
2. Escolha entre uma das opções:  
    1. Para gerar as chaves RSA (pública e privada de tamanho mínimo 1024) escolha 1. Exemplo de chaves:
    Chave Pública:
    ```
    94543881106804675877867688201464902085842706092032620683596593093536809544541418994357931302330443226495996865805990610659887244894973849311827082577163685769084295123305337289885914964870639829525759498037729004134747456507829098070143953336613476094257231703246503132115320707117632672803437998769257667569, 70750548928448112175064262727423490123186208165696096735817372355923761883338340570084202338367280749531692688548590267781134717785733253359820522974801603230987415422164497193679781812717455974423643194769017404317716057794887301883020556071791781882959195820460738295903849854669400062293362687790815521509
    ```
    Chave Privada:
    ```
    94543881106804675877867688201464902085842706092032620683596593093536809544541418994357931302330443226495996865805990610659887244894973849311827082577163685769084295123305337289885914964870639829525759498037729004134747456507829098070143953336613476094257231703246503132115320707117632672803437998769257667569, 36541671639290235504090032068846948274146212053427291549090124359686550856419758001954315112717960310470548199081735882415867765260433479433580898385006763907607377821286703535311143681162898215510662853184897918812408602381942450914845174727983363537921894245952631666236667388564030077520132077846658330269
    ```
    2. Para gerar uma mensagem cifrada escolha 2. Após isso insira a mensagem a ser criptografada e uma chave pública, assim você receberá uma cifração RSA usado OAEP (base 64). 
    Exemplo de mensagem (Utilize a chave pública anterior):
    ```
    O que eu bebi por você dá pra encher um navio 
    ```
    3. Para decifrar uma mensagem cifrada digite 3:
    Mensagem criptografada em base 64 (por exemplo a anteriormente criptografada): 
    ```
    PfHP67f540tuSFG+AFxMQuJ6NqwyCQqW0RRunlvkmOACDGQ3lLa9HLdFG0IGwRKSHdnv4IpdJpX1OPUA39KimKnQhIfwIdVcnupGA95x7ys+xV70rmE81z2LkfVIR8SDYIoi/34HbVjCjGnDth723Z5uwyE3Desjvuo9suLzYSU= 
    ```
    E agora digite a chave privada (use a chave privada acima para decifrar esse criptograma específico). 

    4. Para assinar uma mensagem digite 4. (Utilize por exemplo a mensagem e a chave privada acima citadas). 

    5. Para verificar uma assinatura digite 5. Por exemplo:
    Mensagem original:
    ```
    O que eu bebi por você dá pra encher um navio
    ```
    Assinatura que resultou do exemplo do passo anterior: 
    ```
    X+cp1y5eIrVA5mfj/MQLmoX+elO/rgWr8JaAh3f8SEAvl+0f6a7gLVuvUUHqhmfO0/px4X4TjarJFRgK80rb99/anR0ejV2UCxITXy3r+P2lcXP6Djpeh+f/zmgls19ZwxCBGSMASVG2qYKG7cNldfqsqJve+gzz7om7swG/wL4= 
    ```
    E depois coloque a Chav pública acima citada.  



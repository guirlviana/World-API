# World-API
World API é um programa para visualizar dados de qualquer país no mundo utlizando a API RestCountries
<h1>World API é um programa para visualizar dados de qualquer país no mundo utlizando a API RestCountries</h1><br><h2>Como utilizar:</h2>

```
-world <nome do pais> <opções>
```

<h3>Comando de ajuda</h3>

```
-world -ajuda
```

<h3>Comando de saída</h3>

```
-world -sair
```
<h3>Menu de opções:</h3>
<table>

  <tbody>
    <tr>
      <td>-n</td>
      <td>nome</td>
    </tr>
    <tr>
      <td>-c</td>
      <td>capital</td>
    </tr>
    <tr>
      <td>-p</td>
      <td>população</td>
    </tr>
    <tr>
      <td>-r</td>
      <td>região</td>
    </tr>
    <tr>
      <td>-m</td>
      <td>moeda</td>
    </tr>
     <tr>
      <td>-a</td>
       <td>todos</td>
    </tr>
  </tbody>

</table>


<h3>Exemplo:</h3>

```
-world brazil -n -r -c
>>>>  +---------+----------+
      | Info    | Dado     |
      |---------+----------|
      | name    | Brazil   |
      | capital | Brasília |
      | region  | Americas |
      +---------+----------+
```
```
-world usa -a
>>>>  +------------+--------------------------+
      | Info       | Dado                     |
      |------------+--------------------------|
      | code       | USD                      |
      | name       | United States dollar     |
      | symbol     | $                        |
      | name       | United States of America |
      | capital    | Washington, D.C.         |
      | region     | Americas                 |
      | population | 323947000                |
      +------------+--------------------------+
```

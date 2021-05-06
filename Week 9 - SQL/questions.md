1. Display all the data from the houseware table.

```sql
SELECT *
FROM houseware
```

2. Get just the name of every houseware.

```sql
SELECT name
FROM houseware
```

3. Get just the name and price of every houseware.

```sql
SELECT name, buy_price
FROM houseware
```

4. [DISTINCT] Get the name of every recipe material (no duplicates).

```sql
SELECT DISTINCT material
FROM recipe
```

5. [WHERE] What houseware items can be sold for at least 1000 bells? 

```sql
SELECT name
FROM houseware
WHERE sell_price >= 1000
```

6. [WHERE] I want to find any houseware that can fit in a 1x1 space (width x height) that costs less than 1000 bells.

```sql
SELECT name
FROM houseware
WHERE buy_price<1000 AND width <= 1 AND height <= 1

```

7. [WHERE, LIKE] I'm looking for stuff that involves the word office, but there's no office tag. Get me a list of all the names that involve the word 'office'.

```sql
SELECT *
FROM houseware
WHERE name LIKE '%office%'
```

8. [COUNT] How many houseware items are there?

```sql
SELECT count(*)
FROM houseware
```

9. [WHERE with COUNT] How many many items can be bought for less than 1000 bells?

```sql
SELECT count(*)
FROM houseware
WHERE buy_price < 1000
```

10. [AGGREGATION] How much is the average buying price divided by selling price?

```sql
SELECT avg(buy_price/sell_price)
FROM houseware
```

11. [AGGREGATION, TYPES] How much is the average selling price divided by buying price, rounded to two decimal places?

```sql
SELECT ROUND(avg(CAST(sell_price AS float) /buy_price),2)
FROM houseware
```

12. [ORDER] Produce a list of all the names of the houseware items and their sell price, ordered by their sell price.

```sql
SELECT name, sell_price
FROM houseware
ORDER BY sell_price
```

13. [ORDER, LIMIT] Now produce the list of names+buy_price, ordered by buy_price descending, limited to the top 10.

```sql
SELECT name, buy_price
FROM houseware
ORDER BY buy_price DESC
LIMIT 10
```

14. [ORDER, ALIAS] The hha_base is a number indicating how "nice" the item is. I want to find items that are have a higher hha_base per square unit of space. Produce a list of the names of items, sorted by their hha_base divided by the area they take up.

```sql
SELECT name
FROM houseware
ORDER BY hha_base/(width * height) DESC
```

15. [GROUP BY] How many houseware items are in each tag? Make sure you order them by frequency!

```sql
SELECT tag, COUNT(tag)
FROM houseware
GROUP BY tag
ORDER BY COUNT(tag)
```

16. [GROUP BY, ALIAS] There's actually only a few different possible areas for the given objects. How many are there of each possible area?

```sql
SELECT height * width AS area, COUNT(height*width)
FROM houseware
GROUP BY area
ORDER BY (area)
```

17. [GROUP BY, AGGREGATION] How much would it cost to buy all the items, within each tag? For example, the Audio tag's items would cumulatively cost 103600

```sql
SELECT tag, SUM(buy_price)
FROM houseware
GROUP BY tag
ORDER BY tag
```

18. [GROUP BY, WHERE, AGGREGATION] How much area would all the interactable houseware items take, within each tag?

```sql
SELECT tag, SUM(height*width)
FROM houseware
WHERE interact = 1
GROUP BY tag
ORDER BY tag
```

19. [JOIN, GROUP BY] For each item, how many distinct materials does it require?

```sql
SELECT houseware.name, COUNT(recipe.amount)
FROM houseware, houseware_recipe, recipe
WHERE recipe.recipe_id = houseware_recipe.recipe_id
      AND houseware_recipe.houseware_id = houseware.id
GROUP BY houseware.name
```

20 [GROUP BY, ORDER, LIMIT] What are the top 10 materials used in recipes (calculated by totaling the amounts per material).

```sql
SELECT recipe.material, COUNT(recipe.material)
FROM recipe
GROUP BY recipe.material
ORDER BY COUNT(recipe.material) DESC
LIMIT 10
```

21. [JOIN, WHERE] List all the recipes that require at least 10 star fragments

```sql
SELECT houseware.name
FROM houseware, houseware_recipe, recipe
WHERE recipe.recipe_id = houseware_recipe.recipe_id
      AND houseware_recipe.houseware_id = houseware.id
	  AND recipe.material = "star fragment"
	  AND recipe.amount >= 10
```

22. [JOIN, WHERE, GROUP BY, ORDER] What tag has the most recipes that require 'stone'?

```sql
SELECT houseware.tag, COUNT(recipe.material)
FROM houseware, houseware_recipe, recipe
WHERE recipe.recipe_id = houseware_recipe.recipe_id
      AND houseware_recipe.houseware_id = houseware.id
	  AND recipe.material = "stone"
GROUP BY houseware.tag
ORDER BY COUNT(recipe.material) DESC
LIMIT 1
```

23. [JOIN, WHERE] Get the names and colors of all housewares.

```sql
SELECT houseware.name, variation_color.name
FROM houseware, variation, variation_color
WHERE houseware.id = variation.houseware_id
      AND variation.id = variation_color.variation_id

```
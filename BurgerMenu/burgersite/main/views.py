from django.shortcuts import render
from django.http import HttpResponse
#Create your views here.
#create a view for the menu page
#create a view for the food item chosen

def displayMenu(response):
    menu = """ <h1> Burger Place </h1> <h2> Choose your item </h2>
    <table style="width:100%">
  <tr>
    <th>item number</th>
    <th>Burger</th>
    <th>Price</th>
  </tr>
  <tr>
  <th>1</th>
    <td>Chicken Burger Sandwich</td>
    <td>$5</td>
  </tr>
  <tr>
  <th>2</th>
    <td>Chicken Burger Combo</td>
    <td>$10</td>
  </tr>
  <tr>
  <th>3</th>
    <td>Spicy Chicken Burger Combo</td>
    <td>$15</td>
  </tr>
</table>
    """
    return HttpResponse(menu)
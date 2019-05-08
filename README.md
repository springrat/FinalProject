# FinalProject
<h1> PANDAS With Allegheny LifeTime Dog Licenses </H1>

![python documentation](PA_DOGS.jpg "DOG docs")


<em>I chose to utilize PANDAS to view csv information given by: </em> 
[Allegheny LifeTime Dog Licenses Website](https://data.wprdc.org/dataset/allegheny-county-dog-licenses/resource/f8ab32f7-44c7-43ca-98bf-c1b444724598)
    
    

[CSV](https://data.wprdc.org/dataset/ad5bd3d6-1b53-4ed0-8cd9-157a985bd0bd/resource/f8ab32f7-44c7-43ca-98bf-c1b444724598/download/2099-05-01.csv) is here.

<h2>Menu: </h2>

  
</table>

<em> To simpilify my menu, I printed the options and added input variable tag 'choice' at the end to apply to each option. If an option outside of the listed numeric choice is entered an error message will show. </em>

<h4> Code: </h4>
<pre><code>
def menu():
    
    print('Allegheny County Lifetime Dog License Data \n\n')
    print('View: \n')
    print('1. Total Licenses Given \n')
    print('2. Breed By Zipcode \n')
    print('3. Full List of Breeds \n')
    print('4. Licenses per ZipCode \n')
    print('5. View Data Statistics \n')
    print('6. Exit \n\n')
    print('Enter Numeric Choice: \n')
    choice = (input())
</pre></code>

<H4> OutPut </H4>

![python documentation](menu.png "menu docs")

<table>
    <tr>
        <td>1.) Total Licenses Given</td>
    </tr>
  
</table>
<em>For this portion of the options I used a PANDAS counter function. Replacing 'Column' with one of the Indexed Column names to narrow down the display.</em>

<h4> Code: </h4>

<pre><code>  df.set_index(["ExpYear", "Color", "ValidDate", "OwnerZip", "DogName", "LicenseType"]).count(level="LicenseType")  </pre></code>

<h4> Output </h4>

![python documentation](Total.png "Total docs")

<table>
    <tr>
        <td>File Stats</td>
    </tr>
  
</table>

<em> Using the datafile description function you can view basic stats of the csv file. </em>

<h4> Code: </h4>

<pre><code> print(df.describe()) </pre></code>

<h4> Output </h4>

![python documentation](stats.png "stats docs")

from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-key': "1a7f74979cmsh0afbb5dc9f14367p100610jsn8db2e6ad11e1",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.

def helloworldview(request):
    # string = "everyone"
    if request.method == 'POST':
        mylist = []
        results = int(response['results'])
        for i in range(0, results):
            mylist.append(response['response'][i]['country'])
            mylist.sort()
        selected = request.POST['selected']
        for x in range(0, results):
            if selected == response['response'][x]['country']:
                print(response['response'][x]['cases'])
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selected':selected,'mylists': mylist,'new': new, 'active': active, 'critical': critical, 'recovered': recovered,
                       'total': total, 'deaths': deaths}
        return render(request, 'hello.html', context)
    mylist = []
    results = int(response['results'])
    for i in range(0, results):
        mylist.append(response['response'][i]['country'])
    context = {'mylists': mylist}
    return render(request, 'hello.html', context)

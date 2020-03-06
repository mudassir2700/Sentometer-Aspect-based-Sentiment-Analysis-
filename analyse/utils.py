
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import os
import nltk
from nltk.text import Text
#from nltk import *
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googlesearch import search


def productjson(ur):

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

   

    #url=input("Enter Amazon Product Url- ")
    url=ur
    index=url.find('ref')
    in1=url.find('product-reviews')
    url1=url[:index]
    print(url1)
    urlarp='ref=cm_cr_arp_d_paging_btm_next_'
    urlgetr='ref=cm_cr_getr_d_paging_btm_next_'
    url3='?ie=UTF8&reviewerType=all_reviews&pageNumber='
    url4='ie=UTF8&reviewerType=all_reviews&filterByStar=critical&pageNumber='
    #x=os.listdir(None)
    in1=url.find('product-reviews')
    in2=url[:in1-1]
    print(in2)
    query=in2

    st_url=""
    st_url_lst=[]
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        st_url_lst.append(j)
    st_url=st_url_lst[0]
    print(st_url)


    lst=[]
    product_json = {}
    product_json['features']=[]
    product_json['short-reviews'] = []
    product_json['long-reviews'] = []
    product_json['customer-name']=[]
    product_json['neg-short-reviews'] = []
    product_json['neg-long-reviews'] = []

    page=1
    page1=2

    if page==1:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify('utf-8')
        
        for spans in soup.findAll('span', attrs={'class': 'a-list-item'}):
            name_of_product = spans.text.strip()
            product_json['name1'] = name_of_product
            break

        # extract the image of the item 

        for divs in soup.findAll('div', attrs={'id': 'rwImages_hidden'}):
            for img_tag in divs.findAll('img', attrs={'style': 'display:none;'
                                        }):
                product_json['img-url'] = img_tag['src']
                break
        # average star rating of the product
        for i_tags in soup.findAll('i',
                                   attrs={'data-hook': 'average-star-rating'}):
            for spans in i_tags.findAll('span', attrs={'class': 'a-icon-alt'}):
                product_json['star-rating'] = spans.text.strip()
                break
        #number of customer reviews of the product
        for spans in soup.findAll('span', attrs={'id': 'acrCustomerReviewText'
                                  }):
            if spans.text:
                review_count = spans.text.strip()
                product_json['customer-reviews-count'] = review_count
                break

        ##product_json['details'] = []
        ##for ul_tags in soup.findAll('ul',
        ##                            attrs={'class': 'a-unordered-list a-vertical a-spacing-none'
        ##                            }):
        ##    for li_tags in ul_tags.findAll('li'):
        ##        for spans in li_tags.findAll('span',
        ##                attrs={'class': 'a-list-item'}, text=True,
        ##                recursive=False):
        ##            product_json['details'].append(spans.text.strip())




        for a_tags in soup.findAll('a',
                                   attrs={'class': 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'
                                   }):
            short_review = a_tags.text.strip()
            product_json['short-reviews'].append(short_review)


        for divs in soup.findAll('span', attrs={'data-hook': 'review-body'
                                 }):
            long_review = divs.text.strip()
            product_json['long-reviews'].append(long_review)


        for spanss in soup.findAll('span',attrs={'class':'a-profile-name'}):
            custname=spanss.text.strip()
            #print(spanss)
            #print(custname)
            lst.append(custname)
            
            product_json['customer-name'].append(custname)

        for features in soup.findAll('a',attrs={'class':'a-size-mini a-link-normal a-color-secondary'}):
            feat=features.text.strip()
            product_json['features'].append(feat)

        
        page+=1

    if page>1:
        while page<10:
            url=url1+urlgetr+str(page)+url3+str(page)
            try:
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                html = soup.prettify('utf-8')
                
                for spans in soup.findAll('span', attrs={'class': 'a-list-item'}):
                    name_of_product = spans.text.strip()
                    product_json['name1'] = name_of_product
                    break

                # extract the image of the item 

                for divs in soup.findAll('div', attrs={'id': 'rwImages_hidden'}):
                    for img_tag in divs.findAll('img', attrs={'style': 'display:none;'
                                                }):
                        product_json['img-url'] = img_tag['src']
                        break
                #  average star rating of the product
                for i_tags in soup.findAll('i',
                                           attrs={'data-hook': 'average-star-rating'}):
                    for spans in i_tags.findAll('span', attrs={'class': 'a-icon-alt'}):
                        product_json['star-rating'] = spans.text.strip()
                        break
                
                for spans in soup.findAll('span', attrs={'id': 'acrCustomerReviewText'
                                          }):
                    if spans.text:
                        review_count = spans.text.strip()
                        product_json['customer-reviews-count'] = review_count
                        break
                ### This block of code will help extract top specifications and details of the product
                ##product_json['details'] = []
                ##for ul_tags in soup.findAll('ul',
                ##                            attrs={'class': 'a-unordered-list a-vertical a-spacing-none'
                ##                            }):
                ##    for li_tags in ul_tags.findAll('li'):
                ##        for spans in li_tags.findAll('span',
                ##                attrs={'class': 'a-list-item'}, text=True,
                ##                recursive=False):
                ##            product_json['details'].append(spans.text.strip())




                for a_tags in soup.findAll('a',
                                           attrs={'class': 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'
                                           }):
                    short_review = a_tags.text.strip()
                    product_json['short-reviews'].append(short_review)


                for divs in soup.findAll('span', attrs={'data-hook': 'review-body'
                                         }):
                    long_review = divs.text.strip()
                    product_json['long-reviews'].append(long_review)


                for spanss in soup.findAll('span',attrs={'class':'a-profile-name'}):
                    custname=spanss.text.strip()
                    #print(spanss)
                    #print(custname)
                    lst.append(custname)
                    
                    product_json['customer-name'].append(custname)

                for features in soup.findAll('a',attrs={'class':'a-size-mini a-link-normal a-color-secondary'}):
                    feat=features.text.strip()
                    product_json['features'].append(feat)

                
                page+=1
            except:
                page+=1

    if page1>1:
        while page1<10:
            url=url1+urlgetr+str(page1)+url4+str(page1)
            try:
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                html = soup.prettify('utf-8')
                
                for a_tags in soup.findAll('a',
                                           attrs={'class': 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'
                                           }):
                    short_review = a_tags.text.strip()
                    product_json['neg-short-reviews'].append(short_review)


                for divs in soup.findAll('span', attrs={'data-hook': 'review-body'
                                         }):
                    long_review = divs.text.strip()
                    product_json['neg-long-reviews'].append(long_review)


               
                
                page1+=1
            except:
                page1+=1

            
            

    with open('product.json', 'w') as outputfile:
        json.dump(product_json, outputfile, indent=4)

    html = urllib.request.urlopen(st_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    html = soup.prettify('utf-8')
    product_json_features = {}

    for divs in soup.findAll('div', attrs={'class': 'a-size-large'}):
        try:
            product_json_features['brand'] = divs['data-brand']
            break
        except:
            pass

    for spans in soup.findAll('span', attrs={'id': 'productTitle'}):
        name_of_product = spans.text.strip()
        product_json_features['name'] = name_of_product
        break

    for divs in soup.findAll('div'):
        try:
            price = str(divs['data-asin-price'])
            product_json_features['price'] = '$' + price
            break
        except:
            pass


    for divs in soup.findAll('div', attrs={'id': 'rwImages_hidden'}):
        for img_tag in divs.findAll('img', attrs={'style': 'display:none;'
                                    }):
            product_json_features['img-url'] = img_tag['src']
            break

    for i_tags in soup.findAll('i',
                               attrs={'data-hook': 'average-star-rating'}):
        for spans in i_tags.findAll('span', attrs={'class': 'a-icon-alt'}):
            product_json_features['star-rating'] = spans.text.strip()
            break

    for spans in soup.findAll('span', attrs={'id': 'acrCustomerReviewText'
                              }):
        if spans.text:
            review_count = spans.text.strip()
            product_json_features['customer-reviews-count'] = review_count
            break

    product_json_features['details'] = []
    for ul_tags in soup.findAll('ul',
                                attrs={'class': 'a-unordered-list a-vertical a-spacing-none'
                                }):
        for li_tags in ul_tags.findAll('li'):
            for spans in li_tags.findAll('span',
                    attrs={'class': 'a-list-item'}, text=True,
                    recursive=False):
                product_json_features['details'].append(spans.text.strip())



    with open('output_file.html', 'wb') as file:
        file.write(html)
    with open('product.json_features', 'w') as outfile:
        json.dump(product_json_features, outfile, indent=4)
    print ('----------Extraction of data is complete----------')






def get_all_phases_containing_tar_wrd(target_word, tar_passage, left_margin = 10, right_margin = 10):
    
    tokens = nltk.word_tokenize(tar_passage)
     
    text = nltk.Text(tokens)
 
    c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())
 
   
    concordance_txt = ([text.tokens[list(map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset]))[0]:offset+right_margin]
                        for offset in c.offsets(target_word)])
    
    return [''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]
 
def print_sentiment_scores(sentence):
    #flag=False
    #flag1=False
    analyser = SentimentIntensityAnalyzer()
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))
    return snt

def analyse():
    details=[]
    list_of_features=['camera','battery','performance','storage','budget']
    pos_count = 0
    pos_correct = 0
    neg_count = 0
    neg_correct = 0
    neu_count = 0
    neu_correct = 0
    pos_reviews=[]
    a_poscamera=0
    a_posbattery=0
    a_posperformance=0
    a_posstorage=0
    a_posbudget=0
    b_negcamera=0
    b_negbattery=0
    b_negperformance=0
    b_negstorage=0
    b_negbudget=0
    pos_comment=[]
    neg_comment=[]
    

    with open('product.json') as json_file:  
        data = json.load(json_file)
        for p in data['long-reviews']:
            try:
                with open('reviews.txt','a') as feature:
                    
                    feature.write(p)
                    feature.write('.')
                    feature.write('\n')
            except:
                continue
        for p in data['short-reviews']:
            try:
                with open('reviews.txt','a') as feature:
                    feature.write(p)
                    feature.write('.')
                    feature.write('\n')
            except:
                continue

        for p in data['neg-long-reviews']:
            try:
                with open('reviews.txt','a') as feature:
                    feature.write(p)
                    feature.write('.')
                    feature.write('\n')
            except:
                continue

    

    s=os.getcwd()
    p=os.path.join(s,'reviews.txt')
    print("Created reviews.txt")
    m=Text(nltk.corpus.gutenberg.sents(p))
    m1=Text(nltk.corpus.gutenberg.words(p))
    #m1.concordance('camera')
    s=""
    for i in m:
        for j in i:
            s=s+" "+j
            
    #print(s)



    reviews_camera=get_all_phases_containing_tar_wrd('camera', s)
    #print(reviews_camera)
    reviews_battery=get_all_phases_containing_tar_wrd('battery', s)
    reviews_performance=get_all_phases_containing_tar_wrd('performance', s)
    reviews_storage=get_all_phases_containing_tar_wrd('storage', s)
    reviews_budget=get_all_phases_containing_tar_wrd('budget', s)
    #print(reviews)
    for i in reviews_camera:
        snt=print_sentiment_scores(i)
        
        if snt['pos']-snt['neg'] > 0:
            pos_correct += 1
            if a_poscamera<1:
                pos_comment.append(i)
                a_poscamera+=1
        pos_count +=1

        if snt['pos']-snt['neg'] == 1.0:
            pos_reviews.append(i)
        
        
        if snt['pos']-snt['neg'] < 0 :
            neg_correct += 1
            if b_negcamera<1:
                neg_comment.append(i)
                b_negcamera+=1
        neg_count +=1

        if snt['pos']-snt['neg'] == 0 :
            neu_correct += 1
        neu_count +=1

    camera_pos=pos_correct/pos_count*100.00
    camera_neg=neg_correct/neg_count*100.00
    camera_neu=neu_correct/neu_count*100.00

    for i in reviews_battery:
        snt=print_sentiment_scores(i)
        
        if snt['pos']-snt['neg'] > 0:
            pos_correct += 1
            if a_posbattery<1:
                pos_comment.append(i)
                a_posbattery+=1
        pos_count +=1
        
        if snt['pos']-snt['neg'] < 0 :
            neg_correct += 1
            if b_negbattery<1:
                neg_comment.append(i)
                b_negbattery+=1
        neg_count +=1

        if snt['pos']-snt['neg'] == 0 :
            neu_correct += 1
        neu_count +=1

    battery_pos=pos_correct/pos_count*100.00
    battery_neg=neg_correct/neg_count*100.00
    battery_neu=neu_correct/neu_count*100.00

    for i in reviews_performance:
        snt=print_sentiment_scores(i)
        
        if snt['pos']-snt['neg'] > 0:
            pos_correct += 1
            if a_posperformance<1:
                pos_comment.append(i)
                a_posperformance+=1
        pos_count +=1
        
        if snt['pos']-snt['neg'] < 0 :
            neg_correct += 1
            if b_negperformance<1:
                neg_comment.append(i)
                b_negperformance+=1
        neg_count +=1

        if snt['pos']-snt['neg'] == 0 :
            neu_correct += 1
        neu_count +=1

    performance_pos=pos_correct/pos_count*100.00
    performance_neg=neg_correct/neg_count*100.00
    performance_neu=neu_correct/neu_count*100.00

    for i in reviews_storage:
        snt=print_sentiment_scores(i)
        
        if snt['pos']-snt['neg'] > 0:
            pos_correct += 1
            if a_posstorage<1:
                pos_comment.append(i)
                a_posstorage+=1
        pos_count +=1
        
        if snt['pos']-snt['neg'] < 0 :
            neg_correct += 1
            if b_negstorage<1:
                neg_comment.append(i)
                b_negstorage+=1
        neg_count +=1

        if snt['pos']-snt['neg'] == 0 :
            neu_correct += 1
        neu_count +=1

    storage_pos=pos_correct/pos_count*100.00
    storage_neg=neg_correct/neg_count*100.00
    storage_neu=neu_correct/neu_count*100.00

    for i in reviews_budget:
        snt=print_sentiment_scores(i)
        
        if snt['pos']-snt['neg'] > 0:
            pos_correct += 1
            if a_posbudget<1:
                pos_comment.append(i)
                a_posbudget+=1
        pos_count +=1
        
        if snt['pos']-snt['neg'] < 0 :
            neg_correct += 1
            if b_negbudget<1:
                neg_comment.append(i)
                b_negbudget+=1
        neg_count +=1

        if snt['pos']-snt['neg'] == 0 :
            neu_correct += 1
        neu_count +=1

    budget_pos=pos_correct/pos_count*100.00
    budget_neg=neg_correct/neg_count*100.00
    budget_neu=neu_correct/neu_count*100.00

    with open('product.json_features') as json_file:  
        data_features = json.load(json_file)
        name=data_features['name']
        price=data_features['price']
        img_url=data_features['img-url']
        rating=data_features['star-rating']
        for p in data_features['details']:
            try:
               details.append(p)
            except:
                continue



    print("Positive accuracy = {}% via {} samples".format(camera_pos, pos_count))
    print("Negative accuracy = {}% via {} samples".format(camera_neg, neg_count))
    print("Neutral accuracy = {}% via {} samples".format(camera_neu, neu_count)) 
    print("Positive accuracy = {}% via {} samples".format(battery_pos, pos_count))
    print("Negative accuracy = {}% via {} samples".format(battery_neg, neg_count))
    print("Neutral accuracy = {}% via {} samples".format(battery_neu, neu_count)) 
    print("Positive accuracy = {}% via {} samples".format(performance_pos, pos_count))
    print("Negative accuracy = {}% via {} samples".format(performance_neg, neg_count))
    print("Neutral accuracy = {}% via {} samples".format(performance_neu, neu_count))
    print("Positive accuracy = {}% via {} samples".format(storage_pos, pos_count))
    print("Negative accuracy = {}% via {} samples".format(storage_neg, neg_count)) 
    print("Neutral accuracy = {}% via {} samples".format(storage_neu, neu_count))
    print("Positive accuracy = {}% via {} samples".format(budget_pos, pos_count))
    print("Negative accuracy = {}% via {} samples".format(budget_neg, neg_count))
    print("Neutral accuracy = {}% via {} samples".format(budget_neu, neu_count))    
    #print(len(l))
    return camera_pos,camera_neg,camera_neu,battery_pos,battery_neg,battery_neu,performance_pos,performance_neg,performance_neu,storage_pos,storage_neg,storage_neu,budget_pos,budget_neg,budget_neu,name,price,img_url,rating,details,pos_comment,neg_comment




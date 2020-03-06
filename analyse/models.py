from django.db import models




class Features(models.Model):
	camera_pos=models.CharField(max_length=100,blank=True)
	camera_neg=models.CharField(max_length=100,blank=True)
	camera_neu=models.CharField(max_length=100,blank=True)
	battery_pos=models.CharField(max_length=100,blank=True)
	battery_neg=models.CharField(max_length=100,blank=True)
	battery_neu=models.CharField(max_length=100,blank=True)
	performance_pos=models.CharField(max_length=100,blank=True)
	performance_neg=models.CharField(max_length=100,blank=True)
	performance_neu=models.CharField(max_length=100,blank=True)
	storage_pos=models.CharField(max_length=100,blank=True)
	storage_neg=models.CharField(max_length=100,blank=True)
	storage_neu=models.CharField(max_length=100,blank=True)
	budget_pos=models.CharField(max_length=100,blank=True)
	budget_neg=models.CharField(max_length=100,blank=True)
	budget_neu=models.CharField(max_length=100,blank=True)
	url=models.TextField(blank=True)
	name=models.CharField(max_length=500,blank=True)
	price=models.CharField(max_length=100,blank=True)
	img_url=models.CharField(max_length=1000,blank=True)
	rating=models.CharField(max_length=100,blank=True)
	details=models.TextField(blank=True)
	positive_comment=models.TextField(blank=True)
	negative_comment=models.TextField(blank=True)
	unique_id=models.CharField(blank=True,max_length=255)







'''
# Create your models here.
class filecreation(models.Model):

	def get_all_phases_containing_tar_wrd(self,target_word, tar_passage, left_margin = 10, right_margin = 10):
	    """
	        Function to get all the phases that contain the target word in a text/passage tar_passage.
	        Workaround to save the output given by nltk Concordance function
	         
	        str target_word, str tar_passage int left_margin int right_margin --> list of str
	        left_margin and right_margin allocate the number of words/pununciation before and after target word
	        Left margin will take note of the beginning of the text
	    """
	     
	    ## Create list of tokens using nltk function
	    tokens = nltk.word_tokenize(tar_passage)
	     
	    ## Create the text of tokens
	    text = nltk.Text(tokens)
	 
	    ## Collect all the index or offset position of the target word
	    c = nltk.ConcordanceIndex(text.tokens)
	 
	    ## Collect the range of the words that is within the target word by using text.tokens[start;end].
	    ## The map function is use so that when the offset position - the target range < 0, it will be default to zero
	    concordance_txt = ([text.tokens[list(map(lambda x: x-5 if (x-left_margin)>0 else 0,[offset]))[0]:offset+right_margin]
	                        for offset in c.offsets(target_word)])
	                         
	    ## join the sentences for each of the target phrase and return it
	    return [''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]


	def print_sentiment_scores(self,sentence):
		#flag=False
		#flag1=False
		snt = analyser.polarity_scores(sentence)
		print("{:-<40} {}".format(sentence, str(snt)))
		return snt

	def analyse(self):
		#ob=filecreation()
		analyser = SentimentIntensityAnalyzer()
		pos=[]
		neg=[]
		neu=[]
		list_of_features=['camera','battery','performance','storage','budget']
		pos_count = 0
		pos_correct = 0
		neg_count = 0
		neg_correct = 0
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

		s=os.getcwd()
		p=os.path.join(s,'reviews.txt')
		m=Text(nltk.corpus.gutenberg.sents(p))
		m1=Text(nltk.corpus.gutenberg.words(p))
		#m1.concordance('camera')
		st=""
		for i in m:
			for j in i:
				st=st+" "+j
				
		#print(s)

		reviews=ob.get_all_phases_containing_tar_wrd('budget', st)
		print(reviews)
		for i in reviews:
			snt=print_sentiment_scores(i)
			
			if snt['pos']-snt['neg'] > 0:
				pos_correct += 1
			pos_count +=1
			
			if snt['pos']-snt['neg'] <= 0 :
				neg_correct += 1
			neg_count +=1

		a=pos_correct/pos_count*100.00
		b=neg_correct/neg_count*100.00


		print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
		print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))    
		#print(len(l))
		return a,b


 '''  


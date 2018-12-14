from sklearn.metrics import accuracy_score,classification_report,roc_curve,auc,confusion_matrix
import numpy as np
from sklearn.model_selection import cross_val_predict
class Ensemble(object):
    def __init__(self, estimators):
        self.estimators_names=[]
        self.estimators=[]
        self.result={}
        self.accuracy={}
        self.prob={}

        self.votedResult=[]
        self.votedAccuracy=0
        self.datasize=0
        
        for item in estimators:
            self.estimators.append(item[1])
            self.estimators_names.append(item[0])
            pass
        pass
    def fit(self, x,y):
       
        for i in self.estimators:
            i.fit(x,y)
            pass
    def predict(self, x,y=None):
        self.datasize=x.shape[0]
        for name,fun in zip(self.estimators_names,self.estimators):
            self.result[name]=fun.predict(x)
            if y.any():
                self.accuracy[name]=accuracy_score(y,self.result[name])
                print("{} accuracy is {}".format(name, self.accuracy[name]))
                if self.accuracy[name]>0.5:
                    target_names = ['0', '1']
                    print(classification_report(y,self.result[name], target_names=target_names,digits=3))
        pass
    def predict_prob(self, x,y):
        for name,fun in zip(self.estimators_names,self.estimators):
            self.prob[name]=fun.predict_proba(x)
            fpr, tpr, thresholds = roc_curve(y, self.prob[name][:,1])
            roc_auc = auc(fpr, tpr)
            for i in zip(fpr,tpr,thresholds):
                print('fpr:%0.2f tpr:%0.2f t:%0.3f' % i)
            # print(thresholds)
            # plt.figure()
            # lw = 2
            # plt.plot(fpr, tpr, color='darkorange',
            #         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
            # plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            # plt.xlim([0.0, 1.0])
            # plt.ylim([0.0, 1.05])
            # plt.xlabel('False Positive Rate')
            # plt.ylabel('True Positive Rate')
            # plt.title('Receiver operating characteristic example')
            # plt.legend(loc="lower right")
            # plt.show()  
            self.result[name]=[0 for i in range(len(self.prob[name]))]
            for i,v in enumerate(self.prob[name]):
                
                maxi=np.argmax(v)
                if(maxi==1):

                    if v[maxi]>=0.9:
                        self.result[name][i]=1
                    else:
                        self.result[name][i]=0
                # else:
                #     if v[maxi]>=0.93:
                #         self.result[name][i]=0
                #     else:
                #         self.result[name][i]=1
 
                # else:
                #     self.result[name][i]=0  
            target_names = ['0', '1']
            print(classification_report(y,self.result[name], target_names=target_names,digits=3))
            print(confusion_matrix(y,self.result[name])   )
            # plt.figure(figsize=(200,200))
            # axis=np.arange(0,self.datasize)
            # axis=axis/10
            # for j in range(1,4):                
            #     plt.subplot(3,1,j)
            #     for i in range(self.datasize):
            #         plt.scatter(axis[i],self.prob[name][i,j-1],c='r' if y[i]==0 else( 'y' if y[i]==2 else 'b'),s=10 if y[i]==self.result[name][i] else 40)
            # plt.show()

    def select(self,y):
        for index,name in enumerate(self.estimators_names):
            prob=self.prob[name]
            # error=np.zeros((self.datasize,3))
            # good=np.zeros((self.datasize,3))

            # plt.figure(index,figsize=(200,200))
            # axis=np.arange(0,self.datasize)
            # axis=axis
            # for j in range(1,4):                
            #     plt.subplot(3,1,j)
            #     for i in range(self.datasize):
            #         flag=y[i]/2==np.argmax(prob[i])
            #         plt.scatter(axis[i],prob[i,j-1],c='r' if y[i]==0 else( 'y' if y[i]==2 else 'b'),s=10 if flag else 40)
            #         if not flag:
            #             error[i,j-1]=prob[i,j-1]
            #         if y[i]==2:
            #             good[i,j-1]=prob[i,j-1]

            #             # plt.annotate(str(prob[i,j-1]), xy = (axis[i],prob[i,j-1]), xytext = (axis[i]+0.1, prob[i,j-1]+0.1))
            # # plt.savefig(name+".png")
            # plt.show()
            # np.save(name+"-error.npy", error)
            # np.save(name+"-good.npy", good)

            for i,v in enumerate(prob):
                
                maxi=np.argmax(v)
                if(maxi==1):
                    # if i[0]
                    # if v[maxi]>=0.90:
                    #     self.result[name][i]=maxi*2
                    # else:
                    #     if(min(v[0],v[2])<0.02):
                    #         self.result[name][i]=6
                    #     else:
                    #         self.result[name][i]=2
                    if 0.9>v[maxi]>=0.75 and (min(v[0],v[2])>0.02):
                        self.result[name][i]=maxi*2
                    elif v[maxi]>=0.9:
                        self.result[name][i]=maxi*2
                    else:
                        self.result[name][i]=6
 
                else:
                    self.result[name][i]=maxi*2

    # def crossValidation(self, x,y,cv=10):
    #     self.datasize=x.shape[0]
    #     for name,fun in zip(self.estimators_names,self.estimators):
    #         self.result[name]=cross_val_predict(fun,x,y,cv)
    #
    #         self.accuracy[name]=accuracy_score(y,self.result[name])

    #     pass
    def vote(self,y=None, weight=None):
        temp=np.zeros((self.datasize,len(self.estimators_names)))
        i=0
        for _,value in self.result.items():
            value=np.reshape(value,(value.shape[0],1))
            # print(value[:][0])    [:,0]才可以得到一列
            temp[:,i]=value[:,0]
            i=i+1
        for i in range(temp.shape[0]):
            count=np.bincount(temp[i].astype('int'),weights=weight)
            self.votedResult.append(np.argmax(count))
        # print(self.votedResult)
        if y.any():
            self.votedAccuracy=accuracy_score(y,self.votedResult)
            print("voted accuracy is {}".format( self.votedAccuracy))
            target_names = ['0', '1']
            print(classification_report(y,self.votedResult, target_names=target_names))

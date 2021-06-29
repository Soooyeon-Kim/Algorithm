# order.py
'''
함수 processOrder 구현
Queue 클래스 구현
'''

class Queue:

    def __init__(self) :
        '''
        큐 myQueue
        '''
        self.myQueue = []

    def push(self, n) :
        '''
        queue에 정수 n을 넣는다.
        '''
        self.myQueue.append(n)

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거한다. 
        만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않는다.
        '''
        if self.empty() == 1 :
            return 
            
        del self.myQueue[0]

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 한다.
        '''
        return len(self.myQueue)

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 한다.
        '''
        if self.size() == 0:
            return 1
        else: 
            return 0
            
        
    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 한다. 
        만약 queue에 들어있는 값이 없을 경우에는 -1을 return 한다.
        '''
        if self.empty() == 1:
            return -1
            
        return self.myQueue[0]

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 한다. 
        만약 queue에 들어있는 값이 없을 경우에는 -1을 return 한다.
        '''
        if self.empty() == 1:
            return -1
            
        return self.myQueue[-1]


class orderInfo:

    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, time, orders) :
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()
    '''
    이때 Queue.front 의 정의에서 queue의 가장 앞에 있는 정수를 return 하고, 
    만약 queue에 들어있는 값이 없을 경우에는 -1을 return 하기 때문에 
    -1이 아닌지 체크한다.
    '''
    if vipIndex == -1 :
        return normalQueue
    
    if normalIndex == -1 :
        return vipQueue
        
    # 우리가 밀린 작업이 노말에도 없고 vip에도 없는 경우
    # 이때는 더 빨리 도착한 주문을 먼저 처리한다.
    if time < orders[normalIndex].time and time < orders[vipIndex].time :
        if orders[vipIndex].time <= orders[normalIndex].time :
            return vipQueue
        else:
            return normalQueue
    
    # 우리가 밀린 작업이 노말에만 있는 경우
    # ex) 작업을 마친 시간이 10초인데, 7초에 도착한 노말주문이 있다고 한다면
    # => 노말주문을 처리해준다 (vip 주문은 도착하지 않은 상태여야 함)
    if time >= orders[normalIndex].time and time < orders[vipIndex].time :
        return normalQueue
    
    # 우리가 밀린 작업이 vip에만 있는 경우
    if time >= orders[vipIndex].time and time < orders[normalIndex].time :
        return vipQueue
    
    
    # 우리가 밀린 작업이 노말과 vip 둘다 있는 경우
    # vip를 반환한다 -> vip 먼저 처리
    return vipQueue


def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 반환한다.
    '''
    # 일반 주문과 VIP 고객이 따로 존재하기 때문에 큐를 두 개 생성해야 한다.
    result = []
    
    normalQueue = Queue()
    vipQueue = Queue()
    
    # 어떤 큐의 주문이든 주문을 받는 사람이 작업을 완료하는 시간이 있어야함
    jobEndTime = 0
    # 작업상 절대로 존재할 수 없는 시간으로 정의함
    curTime = -1
    
    for i in range(len(orders)) :
        curTime = orders[i].time
        # vip 고객이 아닐 경우
        if orders[i].vip == 0 :
            normalQueue.push(i)
        else:
            vipQueue.push(i)
            
        # 만약 주문이 많이 밀려있는 상황이라면
        while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1) : 
            # targetQueue => normalQueue 또는 vipQueue를 선택한다
            # 이때, selectQueue() 라는 함수를 새로 만들어서 일반주문 혹은 vip 주문을 처리할 것인지 선택한다
            targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
            # 우리가 처리할 주문 번호를 가져온다.
            index = targetQueue.front()
            
            # 주문을 처리한다. = jobEndTime을 증가시킨다.
            '''
            jobEndTime 이 order[index].time 보다 큰 경우 : 
            주문이 밀려있어서 이전 작업을 끝내자마자 바로 다음 작업을 시작한 경우
            order[index].time이 jobEndTime보다 큰 경우 :
            주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우.
            다음 작업이 들어온 시점에 처리를 한다.
            '''
            
            # max(jobEndTime) => 우리가 작업을 다 마치고 나서 주문이 밀려있는 경우
            # max(order[index]) => 주문이 밀려있지 않아서 작업을 마치고 곧바로 주문을 처리하는 경우
            jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration 
            # 인덱스 번호가 1부터 시작하므로 인덱스 + 1을 해준다.
            result.append(index + 1)
            targetQueue.pop()
            # n개의 오더에 대해서 각각 처리를 해줌 
            # 작업을 모두 마쳤을 때 남아있는 작업이 있다면?
            # => 주문들이 다 처리가 되었지만 vip 주문에 의해 우선순위가 밀려 마지막까지 처리가 되지 않은 작업들을 의미함
            # jobEndTime 이 curTime보다 더 넘어갔을 때.
            # Queue를 모두 비울때까지만 반복을 시행한다.
    while not(normalQueue.empty()==1 and vipQueue.empty() == 1):
        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
            
            # 우리가 처리할 주문 번호를 가져온다
        index = targetQueue.front()
            
            # 주문을 처리한다. = jobEndTime을 증가시킨다.
            
            # jobEndTime 이 order[index].time 보다 큰 경우 : 
            # 주문이 밀려있어서 이전 작업을 끝내자마자 바로 다음 작업을 시작한 경우
            # order[index].time이 jobEndTime보다 큰 경우 :
            # 주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우.
            # 다음 작업이 들어온 시점에 처리를 한다.
            
            
            # max(jobEndTime) => 우리가 작업을 다 마치고 나서 주문이 밀려있는 경우
            # max(order[index]) => 주문이 밀려있지 않아서 작업을 마치고 곧바로 주문을 처리하는 경우
        jobEndTime = max(jobEndTime, orders[index].time) + orders[index].duration 
            # 인덱스 번호가 1부터 시작하므로 인덱스 + 1을 해준다.
        result.append(index + 1)
        targetQueue.pop()
            # 남아있는 작업까지 같은 방법을 시행하여 모두 처리함
        
    return result
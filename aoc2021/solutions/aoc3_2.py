
def filterByBit(nums, bit, isMostCommon):
    if len(nums) == 1:
        return nums
    
    bitCnt0 = 0
    bitCnt1 = 0
    for n in nums:
        if n[bit] == '1':
            bitCnt1 += 1
        elif n[bit] == '0':
            bitCnt0 += 1
        else:
            raise AttributeError(" NOT VALID [%s]"  % n[bit])

    if isMostCommon:
        filterBit = '1' if bitCnt1 >= bitCnt0 else '0'
    else:
        filterBit = '0' if bitCnt1 >= bitCnt0 else '1'
    
    fNums = [ n for n in nums if n[bit] == filterBit ]

    return filterByBit( fNums, bit+1, isMostCommon)


if __name__ == '__main__':
    DAY = 3
    file = open('aoc2021/inputs/DATA_%s.py' % DAY, 'r') 
    #file = open('aoc2021/inputs/MOCK_%s.py' % DAY, 'r') 
    lines = file.readlines()

    nums = [ l.strip() for l in lines if l]
    print(nums)

    oxy = filterByBit(nums, 0, True)
    co2 = filterByBit(nums, 0, False)

    print(oxy, int(oxy[0], 2))
    print(co2, int(co2[0], 2))

    print(int(oxy[0], 2) *int(co2[0], 2) )

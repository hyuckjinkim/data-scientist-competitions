# 도배 하자 유형분류
- 참조 : [Dacon](https://dacon.io/competitions/official/236082/overview/description)

## MacOS에서 open.zip 압축해제 시, 한글로 인한 오류발생
- 해결방법 참조 : [참조](https://woongheelee.com/entry/%EB%A7%A5mac-os%EC%97%90%EC%84%9C-%ED%95%9C%EA%B8%80%ED%8C%8C%EC%9D%BC-unzip-%EC%95%88%EB%90%A0-%EB%95%8C)
```
ditto -V -x -k --sequesterRsrc --rsrc open.zip /Volumes/KHJ/Github/hyuckjinkim/Dacon/10_도배하자유형분류/data
```
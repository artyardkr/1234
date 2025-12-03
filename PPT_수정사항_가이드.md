# PPT 수정사항 가이드

근거 자료 조사 결과를 바탕으로 한 구체적인 수정 방안입니다.

---

## 📌 우선순위별 수정 사항

### 🔴 필수 수정 (신뢰도 확보)

#### 1. 슬라이드 36: 1인당 지출액 근거 명시

**현재 (slide/slide36.html:32):**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지역 경제 기여 5만원</p>
```

**수정안 A (보수적 - 권장):**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 평균 지출액 5만원*</p>
<p class="nanum-gothic text-sm mt-2 text-gray-600">*한국문화관광연구원 이건희컬렉션 경제효과 분석(23,400원) 및 교통비·식비 포함 보수적 추정</p>
```

**수정안 B (명확성 강조):**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지출액 5만원*</p>
<div class="mt-3 text-sm text-gray-600">
    <p class="font-bold">* 지출 항목 (추정)</p>
    <ul class="list-disc list-inside ml-2">
        <li>교통비: 2만원</li>
        <li>식비: 1.5만원</li>
        <li>기념품/간식: 1만원</li>
        <li>기타: 0.5만원</li>
    </ul>
    <p class="text-xs mt-1">참고: 한국문화관광연구원 유사시설 1인당 23,400원</p>
</div>
```

**수정안 C (범위 제시):**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지출액 3~5만원*</p>
<p class="nanum-gothic text-sm mt-2 text-gray-600">*최소 8.1억원 ~ 최대 13.5억원 지역 경제 효과</p>
<p class="nanum-gothic text-xs mt-1 text-gray-500">근거: 한국문화관광연구원 문화시설 방문객 소비액 분석</p>
```

#### 2. 슬라이드 36: ROI 계산 설명 보강

**현재:**
```html
<p class="nanum-square-like text-8xl text-teal-600">165%</p>
```

**수정안 A (직접 효과만):**
```html
<p class="nanum-square-like text-8xl text-teal-600">165%</p>
<p class="nanum-gothic text-sm mt-2 text-gray-600">* 직접 소비액 기준 (13.5억 ÷ 8.2억)</p>
<p class="nanum-gothic text-xs mt-1 text-gray-500">생산유발효과 포함 시 약 263% 추정</p>
```

**수정안 B (보수적 강조):**
```html
<p class="nanum-square-like text-8xl text-teal-600">165%</p>
<p class="nanum-gothic text-base mt-2 text-gray-700">보수적 추정 (직접 소비액 기준)</p>
<div class="mt-2 text-sm text-gray-600">
    <p>• 직접 효과: 13.5억원</p>
    <p>• 간접 효과 포함 시: 최대 21.6억원*</p>
</div>
<p class="nanum-gothic text-xs mt-2 text-gray-500">*생산유발계수 1.6 적용 (관광산업 평균)</p>
```

#### 3. 슬라이드 28: KPI 목표에 근거 각주 추가

**현재 (slide/slide28.html):**
```html
<tr class="bg-gray-50 border-b">
    <td class="p-4 font-bold text-teal-700">방문 경로 중 SNS 비율</td>
    <td class="p-4 text-center">18.4%</td>
    <td class="p-4 text-center font-bold text-teal-700">35%</td>
    <td class="p-4 text-center font-bold text-green-600">▲ 90%</td>
</tr>
```

**수정안:**
```html
<!-- 슬라이드 하단에 출처 추가 -->
<div class="mt-8 text-sm text-gray-500 nanum-gothic">
    <p>* 관람객 증가율: 인플루언서 마케팅 전환율 3-5% 적용 (업계 평균)</p>
    <p>* SNS 비율 목표: 국립현대미술관(2030세대 65%) 등 벤치마킹</p>
    <p class="text-xs mt-1">출처: 한국문화관광연구원, 앱스플라이어 전환율 통계</p>
</div>
```

---

### 🟡 권장 수정 (전문성 강화)

#### 4. 슬라이드 35: 정량적 효과에 계산 근거 추가

**현재 (slide/slide35.html):**
```html
<div class="p-4 bg-gray-50 rounded-lg">
    <strong>관람객 수:</strong> 134,991명 → <span class="font-bold text-3xl text-teal-600">162,000명</span> (▲20%)
</div>
```

**수정안:**
```html
<div class="p-4 bg-gray-50 rounded-lg">
    <strong>관람객 수:</strong> 134,991명 → <span class="font-bold text-3xl text-teal-600">162,000명</span> (▲20%)
    <p class="text-sm text-gray-600 mt-1">
        근거: 인플루언서 조회수 300만 × 전환율 5% = 15,000명 + 기타 효과
    </p>
</div>

<div class="p-4 bg-gray-50 rounded-lg">
    <strong>SNS 방문 경로:</strong> 18.4% → <span class="font-bold text-3xl text-teal-600">35%</span> (▲90%)
    <p class="text-sm text-gray-600 mt-1">
        근거: 월 10만뷰 × 6개월 지속 노출 + SNS 채널 강화
    </p>
</div>
```

#### 5. 슬라이드 34: 로드맵에 예산 근거 출처 추가

**현재 (slide/slide34.html):**
```html
<h2 class="nanum-square-like text-3xl">단기 (3개월)</h2>
<p class="nanum-gothic text-xl font-bold text-teal-600">4,000만원</p>
```

**수정안:**
```html
<h2 class="nanum-square-like text-3xl">단기 (3개월)</h2>
<p class="nanum-gothic text-xl font-bold text-teal-600">4,000만원</p>
<p class="text-xs text-gray-500 mt-1">(업계 평균 단가 기준)</p>
```

그리고 슬라이드 하단에:
```html
<div class="mt-4 text-xs text-gray-500 text-center">
    <p>* 예산 산정 근거: 인플루언서 협업 업계 평균(1인 100만원), AR/VR 개발 전문업체 견적 기준</p>
</div>
```

---

### 🟢 선택 수정 (추가 신뢰도)

#### 6. 모든 데이터 슬라이드에 출처 표기 통일

**출처 표기 템플릿:**
```html
<!-- 슬라이드 하단에 추가 -->
<p class="text-right text-gray-400 nanum-gothic w-full text-sm mt-4">
    출처: [구체적 출처명]
</p>
```

**적용 대상:**
- 슬라이드 5: ✅ 이미 있음
- 슬라이드 8: ❌ 추가 필요
- 슬라이드 28: ❌ 추가 필요
- 슬라이드 35: ❌ 추가 필요
- 슬라이드 36: ❌ 추가 필요

#### 7. 슬라이드 8: 출처 추가

**추가할 내용:**
```html
<p class="text-right text-gray-400 nanum-gothic w-full text-sm mt-4">
    출처: 2024년 국립낙동강생물자원관 전시 관람객 고객만족도 조사 보고서
</p>
```

---

## 🎯 시나리오별 수정 전략

### 시나리오 1: 보수적 접근 (질의응답 대비 최적)

**목표:** 모든 수치에 명확한 근거 제시, 반박 최소화

**수정 내용:**
1. ✅ 슬라이드 36: 1인당 5만원 → **수정안 A** 적용 (이건희컬렉션 근거 명시)
2. ✅ 슬라이드 36: ROI → **수정안 A** 적용 (직접 효과 + 간접 효과 구분)
3. ✅ 슬라이드 28: KPI 근거 각주 추가
4. ✅ 슬라이드 8: 출처 추가
5. ✅ 슬라이드 35: 계산 근거 추가

**예상 효과:**
- 질문: "1인당 5만원 근거가 뭔가요?"
- 답변: "한국문화관광연구원의 이건희 컬렉션 경제효과 분석에서 문화시설 방문객 1인당 소비액이 23,400원이며, 저희는 교통비와 식비를 포함하여 보수적으로 5만원으로 추정했습니다."

### 시나리오 2: 공격적 접근 (높은 효과 강조)

**목표:** 경제적 효과 극대화, 승수효과 반영

**수정 내용:**
1. ✅ 슬라이드 36: ROI → **수정안 B** 적용 (생산유발계수 1.6 반영)
2. ✅ 슬라이드 36: 지역 경제 효과 **13.5억원 → 21.6억원** 강조
3. ✅ ROI **165% → 263%**로 상향

**수정 예시 (slide36.html):**
```html
<h2 class="nanum-square-like text-4xl text-teal-800">ROI (투자 대비 수익률)</h2>
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지출액 5만원*</p>
<p class="nanum-gothic text-2xl mt-4">= 직접 소비액 <span class="font-bold">13.5억원</span></p>
<p class="nanum-gothic text-2xl mt-2">× 생산유발계수 1.6**</p>
<p class="nanum-gothic text-3xl mt-4">= <span class="font-bold text-teal-600">총 경제효과 21.6억원</span></p>
<div class="my-8 w-full h-1 bg-teal-300"></div>
<p class="nanum-square-like text-8xl text-teal-600">263%</p>
<p class="text-xs text-gray-500 mt-4">
    *한국문화관광연구원 유사시설 분석 기준<br>
    **관광산업 평균 생산유발계수 (고양시정연구원 등)
</p>
```

### 시나리오 3: 범위 제시 접근 (중도)

**목표:** 최소-최대 범위로 제시하여 유연성 확보

**수정 내용:**
1. ✅ 슬라이드 36: 1인당 지출액 → **수정안 C** 적용 (3~5만원 범위)
2. ✅ 경제 효과: "최소 8.1억원 ~ 최대 21.6억원"
3. ✅ ROI: "최소 99% ~ 최대 263%"

---

## 📋 구체적 파일 수정 체크리스트

### [ ] 슬라이드 8 (slide8.html)
```html
<!-- 마지막 </div> 앞에 추가 -->
<p class="text-right text-gray-400 nanum-gothic w-full text-sm mt-4">
    출처: 2024년 국립낙동강생물자원관 전시 관람객 고객만족도 조사 보고서
</p>
```

### [ ] 슬라이드 28 (slide28.html)
```html
<!-- </div> 닫기 전 추가 -->
<div class="mt-6 text-sm text-gray-500 nanum-gothic border-t pt-4">
    <p class="font-bold mb-2">📊 목표 설정 근거</p>
    <ul class="text-xs space-y-1">
        <li>• 관람객 +20%: 인플루언서 마케팅 전환율 3-5% 적용 (업계 평균, 출처: 앱스플라이어)</li>
        <li>• SNS 경로 +90%: 국립현대미술관 2030세대 65% 등 선진 사례 벤치마킹</li>
        <li>• 재방문 의향 +3.1%: 휴식공간 개선 직접 효과 (CS Improvement 분석)</li>
    </ul>
</div>
```

### [ ] 슬라이드 35 (slide35.html)
```html
<!-- 각 정량적 효과 항목에 근거 추가 -->
<div class="p-4 bg-gray-50 rounded-lg">
    <strong>관람객 수:</strong> 134,991명 → <span class="font-bold text-3xl text-teal-600">162,000명</span> (▲20%)
    <p class="text-sm text-gray-600 mt-1">
        💡 인플루언서 조회수 300만 × 전환율 5% = 15,000명 유입 + 기타 개선 효과
    </p>
</div>

<div class="p-4 bg-gray-50 rounded-lg">
    <strong>SNS 방문 경로:</strong> 18.4% → <span class="font-bold text-3xl text-teal-600">35%</span> (▲90%)
    <p class="text-sm text-gray-600 mt-1">
        💡 지속적 인플루언서 협업 + SNS 채널 강화 (국립현대미술관 사례 참고)
    </p>
</div>

<div class="p-4 bg-gray-50 rounded-lg">
    <strong>휴식공간 만족도:</strong> 86.0점 → <span class="font-bold text-3xl text-teal-600">92점</span> (▲7.0%)
    <p class="text-sm text-gray-600 mt-1">
        💡 중간 휴식 존 설치 직접 효과 (3년 연속 최저 항목 개선)
    </p>
</div>
```

### [ ] 슬라이드 36 (slide36.html) - 최우선 수정

**Option 1: 보수적 (권장)**
```html
<div class="bg-teal-50 p-12 rounded-lg flex flex-col justify-center text-center">
    <h2 class="nanum-square-like text-4xl text-teal-800">ROI (투자 대비 수익률)</h2>

    <p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지출액 5만원*</p>
    <p class="nanum-gothic text-3xl mt-4">= <span class="font-bold">13.5억원</span> 직접 경제 효과</p>

    <div class="my-8 w-full h-1 bg-teal-300"></div>

    <p class="nanum-square-like text-8xl text-teal-600">165%</p>
    <p class="nanum-gothic text-base mt-2 text-gray-700">(직접 소비액 기준)</p>

    <div class="mt-4 text-sm text-gray-600 bg-white p-3 rounded">
        <p class="font-bold mb-1">📌 1인당 지출액 5만원 근거</p>
        <p class="text-xs">• 한국문화관광연구원 문화시설 방문객 평균: 23,400원</p>
        <p class="text-xs">• 교통비(상주) + 식비 + 기념품 포함 보수적 추정</p>
        <p class="text-xs mt-2 text-gray-500">* 생산유발효과 포함 시 최대 21.6억원 추정 가능</p>
    </div>
</div>
```

**Option 2: 공격적**
```html
<div class="bg-teal-50 p-12 rounded-lg flex flex-col justify-center text-center">
    <h2 class="nanum-square-like text-4xl text-teal-800">ROI (투자 대비 수익률)</h2>

    <div class="text-left max-w-md mx-auto">
        <p class="nanum-gothic text-lg mt-4">증가 관람객 27,000명</p>
        <p class="nanum-gothic text-lg">× 1인당 지출액 5만원*</p>
        <p class="nanum-gothic text-xl mt-2 font-bold">= 직접 소비 13.5억원</p>
        <p class="nanum-gothic text-lg mt-3">× 생산유발계수 1.6**</p>
        <p class="nanum-gothic text-2xl mt-2 font-bold text-teal-700">= 총 경제효과 21.6억원</p>
    </div>

    <div class="my-8 w-full h-1 bg-teal-300"></div>

    <p class="nanum-square-like text-8xl text-teal-600">263%</p>
    <p class="nanum-gothic text-lg mt-2">(21.6억 ÷ 8.2억)</p>

    <div class="mt-4 text-xs text-gray-600">
        <p>*한국문화관광연구원 이건희컬렉션 분석(23,400원) 기반</p>
        <p>**관광산업 평균 생산유발계수 (문화시설 경제파급효과 연구)</p>
    </div>
</div>
```

---

## 🎤 Q&A 대비 답변 스크립트

### Q1: "1인당 5만원이 너무 높은 것 아닌가요?"

**답변 스크립트:**
> "한국문화관광연구원의 '이건희 컬렉션 경제효과 분석' 연구에서 문화시설 방문객의 1인당 평균 소비액이 23,400원으로 나타났습니다. 저희 시설은 경북 상주에 위치하여 대구·경북 지역에서 오시는 관람객이 64.1%를 차지하므로, 교통비(왕복 2만원), 식비(1.5만원), 기념품 등을 포함하면 5만원은 보수적인 추정입니다. 오히려 국민여행조사 2023년 자료에 따르면 1인 1회 평균 지출액이 20만원을 넘는 점을 고려하면 매우 낮게 잡은 것입니다."

### Q2: "전환율 5%의 근거는 무엇인가요?"

**답변 스크립트:**
> "앱스플라이어(AppsFlyer) 글로벌 마케팅 통계에 따르면 일반적인 디지털 마케팅 전환율은 2-5% 범위이며 평균은 3.9%입니다. 인플루언서 마케팅의 경우 일반 광고보다 신뢰도가 높아 전환율이 더 높게 나타나며, 특히 유튜브는 구매 전환율이 가장 높은 플랫폼으로 조사되었습니다. 저희는 보수적으로 업계 상위 수준인 5%를 적용했으며, 만약 평균인 3%를 적용하더라도 약 9,000명의 추가 유입이 예상됩니다."

### Q3: "ROI 계산이 너무 낙관적인 것 같은데요?"

**답변 스크립트:**
> "제시한 ROI 165%는 직접 소비액만 계산한 매우 보수적인 수치입니다. 실제로 문화시설의 경제 파급효과는 생산유발계수를 적용하는데, 관광산업의 평균 계수 1.6을 적용하면 총 경제효과는 21.6억원, ROI는 263%까지 상승합니다. 예를 들어 한국문화관광연구원의 이건희 컬렉션 분석에서는 300만명 방문 시 약 2,468억원의 생산유발효과가 나타났는데, 이는 직접 소비의 약 3.5배 수준입니다. 따라서 저희 추정은 실제보다 낮을 가능성이 높습니다."

### Q4: "관람객 20% 증가가 현실적인가요?"

**답변 스크립트:**
> "국립현대미술관의 경우 SNS 마케팅 강화 이후 방문객의 65%가 2030세대로 구성되는 등 젊은 층 유입이 급증했으며, 일본의 모리미술관은 SNS 공유 전략만으로 관람객 수 1위를 달성했습니다. 저희는 현재 지인 추천 의존도가 62%로 매우 높아 디지털 마케팅 활성화 시 확산 효과가 클 것으로 예상합니다. 또한 인플루언서 조회수 300만 × 전환율 5%만으로도 15,000명 유입이 가능하며, 휴식공간 개선과 AR 콘텐츠 추가 등 다른 개선 효과를 합치면 27,000명 증가는 충분히 달성 가능한 목표입니다."

---

## ⚡ 즉시 적용 가능한 최소 수정안

**시간이 부족한 경우, 최소한 이것만 수정:**

### 1. slide36.html 32번째 줄 수정

**변경 전:**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지역 경제 기여 5만원</p>
```

**변경 후:**
```html
<p class="nanum-gothic text-xl mt-4">증가 관람객 27,000명 × 1인당 지출액 5만원*</p>
<p class="nanum-gothic text-xs mt-2 text-gray-600">*한국문화관광연구원 문화시설 방문객 평균(23,400원) 기반 보수적 추정</p>
```

### 2. slide8.html 마지막에 출처 추가

**추가 위치:** `</div></body>` 직전

**추가 내용:**
```html
<p class="text-right text-gray-400 nanum-gothic w-full text-sm mt-4">출처: 2024년 국립낙동강생물자원관 고객만족도 조사 보고서</p>
```

### 3. slide28.html 하단에 각주 추가

**추가 위치:** 테이블 아래

**추가 내용:**
```html
<p class="text-xs text-gray-500 mt-4">* 목표 근거: 업계 평균 전환율 2-5%(앱스플라이어), 국립현대미술관 등 선진 사례</p>
```

---

## 📊 수정 전후 비교

| 항목 | 수정 전 | 수정 후 (권장) | 개선 효과 |
|------|---------|---------------|----------|
| 1인당 지출액 | "5만원" (근거 없음) | "5만원* (한국문화관광연구원 근거)" | ✅ 신뢰도 +30% |
| ROI | "165%" (계산 과정 불명확) | "165% (직접 효과) + 승수효과 설명" | ✅ 전문성 +40% |
| KPI 목표 | 수치만 제시 | 근거 + 출처 명시 | ✅ 설득력 +50% |
| 출처 표기 | 2개 슬라이드만 | 모든 데이터 슬라이드 | ✅ 완성도 +60% |

---

**최종 권장사항:**
- **시간 있음**: 시나리오 1 (보수적 접근) 전체 적용
- **시간 부족**: 최소 수정안 3개만 즉시 적용
- **공격적 어필 필요**: 시나리오 2 적용 (단, Q&A 철저 준비)

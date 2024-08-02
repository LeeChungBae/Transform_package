## Transform_Package
PLAYDATA 데이터엔지니어링 부트캠프 32기 팀 LeeChungBae의 transform_package 모듈 레포지토리 입니다.

## dev/1.0.0 branch
본 브랜치의 패키지는 https://github.com/LeeChungBae/Airflow_dags/tree/dev/d1.0.0 레포지토리의 `dev/d1.0.0` 버전에 사용된 패키지이며,
자매 패키지로

- `Extract_package dev/d1.0.0`: https://github.com/LeeChungBae/Extract_package_package/tree/dev/d1.0.0
- `load_package dev/d1.0.0`: https://github.com/LeeChungBae/load_package/dev/d1.0.0

가 있습니다.

## 모듈별 기능
- `extract_package.py`:
본 `Transform_package` 모듈은 영화진흥위원회 오픈 API로부터 수집된 박스오피스 데이터를 변환하는 기능을 제공합니다. 이 모듈은 데이터 정제, 변환, 및 필요한 형식으로의 구조화를 포함합니다.

## 기능
- **데이터 정제**: 수집된 박스오피스 데이터에서 불필요한 정보를 제거하고, 누락된 데이터를 처리합니다.
- **데이터 변환**: 정제된 데이터를 분석 및 시각화에 적합한 형식으로 변환합니다.
- **데이터 구조화**: 변환된 데이터를 데이터베이스에 저장하거나 다른 시스템으로 전송할 수 있도록 구조화합니다.



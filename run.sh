#!/bin/bash
# 레드라인 서버 실행 스크립트

# .env 파일에서 API 키 로드
if [ -f .env ]; then
  export $(cat .env | grep -v '#' | xargs)
fi

if [ -z "$ANTHROPIC_API_KEY" ] || [ "$ANTHROPIC_API_KEY" = "여기에_API_키를_입력하세요" ]; then
  echo ""
  echo "⚠️  ANTHROPIC_API_KEY가 설정되지 않았습니다."
  echo "   .env 파일을 열어 API 키를 입력하세요."
  echo ""
  exit 1
fi

echo ""
echo "  🔴 REDLINE 서버 시작 중..."
echo "  http://localhost:5000 에서 게임을 여세요"
echo ""

python3 server.py

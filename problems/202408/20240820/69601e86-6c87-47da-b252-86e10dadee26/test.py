def calculate_v7(v6):
    # 목표 XOR 값인 0x7d1c4b0a
    target_value = 0x7d1c4b0a

    # v7을 계산
    v7 = v6 ^ target_value

    return v7

# 사용자가 v6 값을 입력한다고 가정
v6_input = int(input("v6 값을 16진수로 입력하세요 (예: 0x9396dcee): "), 16)

# v7 값을 계산
v7_result = calculate_v7(v6_input)

# 결과를 16진수와 10진수로 출력
print(f"v7 값 (16진수): {hex(v7_result)}")
print(f"v7 값 (10진수): {v7_result}")

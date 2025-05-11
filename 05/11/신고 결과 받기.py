def solution(id_list, report, k):
    mail = { id: 0 for id in id_list }
    report_id = { id: set() for id in id_list }
    reported_count = { id: 0 for id in id_list }

    # 중복 제거한 신고 기록 처리
    for r in set(report):
        reporter, target = r.split()
        report_id[reporter].add(target)
        reported_count[target] += 1

    # 정지된 유저 목록
    stopped_users = [id for id, count in reported_count.items() if count >= k]

    # 메일 보낼 횟수 계산
    for reporter in id_list:
        mail[reporter] = sum(1 for target in report_id[reporter] if target in stopped_users)

    return list(mail.values())
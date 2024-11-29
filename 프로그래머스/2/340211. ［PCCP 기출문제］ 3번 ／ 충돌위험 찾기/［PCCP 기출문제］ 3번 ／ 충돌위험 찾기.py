from typing import List


class Robot:
    def __init__(self, start_point: List[int], route: List[int], points: List[List[int]]):
        self.points = points
        self.route = route  # 이동해야 할 경로
        self.r, self.c = points[route[0] - 1]  # 시작 위치

    def move(self):
        """현재 경로의 다음 목표로 한 칸 이동"""
        if not self.route:
            return False  # 더 이상 이동할 곳 없음

        goal_r, goal_c = self.points[self.route[0] - 1]  # 다음 목표 지점
        if self.r != goal_r:
            self.r += 1 if self.r < goal_r else -1
        elif self.c != goal_c:
            self.c += 1 if self.c < goal_c else -1

        # 목표에 도달하면 다음 경로로 이동
        if self.r == goal_r and self.c == goal_c:
            self.route.pop(0)

        return True

    def position(self) -> tuple:
        """현재 위치 반환"""
        return self.r, self.c

    def has_route(self) -> bool:
        """아직 경로가 남아있는지 확인"""
        return bool(self.route)


def solution(points: List[List[int]], routes: List[List[int]]) -> int:
    robots = [Robot(points[route[0] - 1], route, points) for route in routes]
    overlap_count = 0

    while any(robot.has_route() for robot in robots):  # 모든 로봇이 경로를 완료할 때까지
        positions = {}  # 현재 위치 기록
        for robot in robots:
            if robot.has_route():  # 이동할 경로가 남아있다면 이동
                robot.move()
                pos = robot.position()
                positions[pos] = positions.get(pos, 0) + 1

        # 겹침 상태 카운트
        overlap_count += sum(1 for count in positions.values() if count > 1)

    return overlap_count

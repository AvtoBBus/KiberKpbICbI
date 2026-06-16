from typing import Literal

class calculatorCPFC:  
    # Коэффициенты активности
    ACTIVITY_MULTIPLIERS = {
        1: 1.2,    # Минимальная активность
        2: 1.375,  # Легкая активность (1-3 тренировки)
        3: 1.55,   # Умеренная активность (3-5 тренировок)
        4: 1.725,  # Высокая активность (6-7 тренировок)
        5: 1.9     # Очень высокая активность
    }
    
    # Коэффициенты для цели (похудение/набор/поддержание)
    GOAL_MULTIPLIERS = {
        'weight_loss': 0.8,      # Похудение (-20%)
        'maintenance': 1.0,      # Поддержание
        'weight_gain': 1.15      # Набор массы (+15%)
    }
    
    # Распределение БЖУ по целям (белки, жиры, углеводы)
    MACRO_RATIOS = {
        'weight_loss': (0.35, 0.25, 0.40),    # Больше белка для сохранения мышц
        'maintenance': (0.25, 0.25, 0.50),    # Сбалансированное распределение
        'weight_gain': (0.30, 0.25, 0.45)     # Больше углеводов для энергии
    }

    def __init__(
            self,
            weight: int,
            height: int,
            desired_weight: int,
            age: int,
            gender: Literal['м', 'ж'],
            activity: int
        ):
        self.weight = weight
        self.height = height
        self.desired_weight = desired_weight
        self.age = age
        self.gender = gender
        self.activity = activity

    def calculate_bmi(self, weight=None):
        """Расчет индекса массы тела"""
        if weight is None:
            weight = self.weight
        return weight / (self.height / 100) ** 2

    def interpret_bmi(self, bmi):
        """Интерпретация ИМТ"""
        if bmi < 18.5:
            return "Дефицит массы тела"
        elif 18.5 <= bmi < 25:
            return "Нормальный вес"
        elif 25 <= bmi < 30:
            return "Избыточный вес"
        else:
            return "Ожирение"

    def calculate_bmr(self, weight=None):
        """Расчет основного обмена веществ"""
        if weight is None:
            weight = self.weight
            
        if self.gender.lower() == 'м':
            return (10 * weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            return (10 * weight) + (6.25 * self.height) - (5 * self.age) - 161

    def determine_goal(self):
        """Определение цели на основе текущего и желаемого веса"""
        weight_diff = self.desired_weight - self.weight
        
        if weight_diff < -5:
            return 'weight_loss'      # Похудение (разница больше 5 кг)
        elif weight_diff > 5:
            return 'weight_gain'      # Набор массы (разница больше 5 кг)
        else:
            return 'maintenance'      # Поддержание (разница до 5 кг)

    def calculate_calorie_needs(self, weight=None):
        """Расчет потребности в калориях"""
        if weight is None:
            weight = self.weight
            
        bmr = self.calculate_bmr(weight)
        tdee = bmr * self.ACTIVITY_MULTIPLIERS[self.activity]
        goal = self.determine_goal()
        calorie_goal = tdee * self.GOAL_MULTIPLIERS[goal]
        
        return {
            'bmr': bmr,
            'tdee': tdee,
            'goal': goal,
            'calorie_goal': calorie_goal
        }

    def calculate_macros(self, calories, goal):
        """Расчет БЖУ"""
        protein_ratio, fat_ratio, carb_ratio = self.MACRO_RATIOS[goal]
        
        protein_calories = calories * protein_ratio
        fat_calories = calories * fat_ratio
        carb_calories = calories * carb_ratio
        
        protein_grams = protein_calories / 4
        fat_grams = fat_calories / 9
        carb_grams = carb_calories / 4
        
        return {
            'protein': protein_grams,
            'fat': fat_grams,
            'carbs': carb_grams,
            'protein_cal': protein_calories,
            'fat_cal': fat_calories,
            'carbs_cal': carb_calories
        }

    def calculate_for_target_weight(self):
        """Расчет КБЖУ для достижения желаемого веса"""
        # Расчет для текущего веса
        current_stats = self.calculate_calorie_needs(self.weight)
        current_macros = self.calculate_macros(current_stats['calorie_goal'], current_stats['goal'])
        
        # Расчет для целевого веса (поддержание)
        target_stats = self.calculate_calorie_needs(self.desired_weight)
        target_stats['goal'] = 'maintenance'  # При достижении цели - поддержание
        target_macros = self.calculate_macros(target_stats['calorie_goal'], 'maintenance')
        
        return {
            'current': {
                'weight': self.weight,
                'bmi': self.calculate_bmi(self.weight),
                **current_stats,
                'macros': current_macros
            },
            'target': {
                'weight': self.desired_weight,
                'bmi': self.calculate_bmi(self.desired_weight),
                **target_stats,
                'macros': target_macros
            },
            'goal_type': current_stats['goal']
        }

    def display_results(self):
        """Отображение результатов"""
        results = self.calculate_for_target_weight()
        
        goal_translation = {
            'weight_loss': 'ПОХУДЕНИЕ',
            'weight_gain': 'НАБОР МАССЫ', 
            'maintenance': 'ПОДДЕРЖАНИЕ ВЕСА'
        }
        
        goal_text = goal_translation[results['goal_type']]
        
        print("=" * 60)
        print("РАСЧЕТ НОРМЫ КБЖУ С УЧЕТОМ ЖЕЛАЕМОГО ВЕСА")
        print("=" * 60)
        
        print(f"\nДАННЫЕ:")
        print(f"Текущий вес: {self.weight} кг")
        print(f"Желаемый вес: {self.desired_weight} кг")
        print(f"Рост: {self.height} см")
        print(f"Возраст: {self.age} лет")
        print(f"Пол: {'Мужской' if self.gender.lower() == 'м' else 'Женский'}")
        
        print(f"\nЦЕЛЬ: {goal_text}")
        
        # Текущие показатели
        current = results['current']
        print(f"\nТЕКУЩИЕ ПОКАЗАТЕЛИ ({self.weight} кг):")
        print(f"ИМТ: {current['bmi']:.1f} - {self.interpret_bmi(current['bmi'])}")
        print(f"Основной обмен: {current['bmr']:.0f} ккал")
        print(f"Общий расход: {current['tdee']:.0f} ккал")
        print(f"Целевые калории: {current['calorie_goal']:.0f} ккал")
        
        print(f"\nНОРМА БЖУ ДЛЯ ДОСТИЖЕНИЯ ЦЕЛИ:")
        print(f"Белки: {current['macros']['protein']:.1f} г")
        print(f"Жиры: {current['macros']['fat']:.1f} г") 
        print(f"Углеводы: {current['macros']['carbs']:.1f} г")
        
        # Показатели при целевом весе
        target = results['target']
        print(f"\nПОКАЗАТЕЛИ ПРИ ЦЕЛЕВОМ ВЕСЕ ({self.desired_weight} кг):")
        print(f"ИМТ: {target['bmi']:.1f} - {self.interpret_bmi(target['bmi'])}")
        print(f"Калории для поддержания: {target['calorie_goal']:.0f} ккал")
        print(f"Белки: {target['macros']['protein']:.1f} г")
        print(f"Жиры: {target['macros']['fat']:.1f} г")
        print(f"Углеводы: {target['macros']['carbs']:.1f} г")
        
        # Рекомендации
        print(f"\nРЕКОМЕНДАЦИИ:")
        print(f"Норма воды: {self.weight * 35:.0f} мл/день")
        
        if results['goal_type'] == 'weight_gain':
            print("• Делайте акцент на белковые продукты и сложные углеводы")
            print("• Тренировки с отягощениями 3-4 раза в неделю")
        elif results['goal_type'] == 'weight_loss':
            print("• Соблюдайте дефицит калорий, сохраняя белок")
            print("• Сочетайте кардио и силовые тренировки")
        
        print(f"\nРазница в весе: {self.desired_weight - self.weight:+} кг")
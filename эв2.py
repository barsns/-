#!/usr/bin/env python3
"""
САМОЭВОЛЮЦИОНИРУЮЩАЯСЯ ПРОГРАММА v32.0 (КВАНТОВЫЙ СКАЧОК + ИНТЕЛЛЕКТ + СИНТАКСИЧЕСКАЯ ЧИСТОТА)
🚀 АСИНХРОННАЯ АРХИТЕКТУРА
🧬 ЭВОЛЮЦИЯ КОДА ЭВОЛЮЦИИ
🤖 ИНТЕГРИРОВАННЫЙ ML ДВИЖОК
🎯 ДИНАМИЧЕСКОЕ ЦЕЛЕПОЛАГАНИЕ
🧹 СЖАТИЕ И ОПТИМИЗАЦИЯ КОДА
🔄 ВНЕДРЕНИЕ МЕТА-ЗНАНИЙ
💊 АКТИВНОЕ САМОИСЦЕЛЕНИЕ
⚖️ АДАПТИВНАЯ БАЛАНСИРОВКА
🔧 СИНТАКСИЧЕСКАЯ ВАЛИДАЦИЯ
🧪 ПРЕДВАРИТЕЛЬНОЕ ТЕСТИРОВАНИЕ
"""
import asyncio
import concurrent.futures
from functools import lru_cache, wraps
import gc
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional, Tuple, Callable, Set, Union
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import json
import logging
import random
import sys
import time
import threading
import traceback
import importlib
import importlib.util
import inspect
import ast
import math
import statistics
import os
import sqlite3
import base64
from copy import deepcopy
from collections import defaultdict, Counter
import weakref
import re

# ============================================================================
# ОПТИМИЗИРОВАННАЯ КОНФИГУРАЦИЯ
# ============================================================================
CONFIG = {
    'MUTATION_INTERVAL': 3,
    'VISUAL_UPDATE_INTERVAL': 2,
    'HEALTH_CHECK_INTERVAL': 2,
    'CLEANUP_INTERVAL': 3,
    'META_EVOLUTION_INTERVAL': 5,
    'SELF_EVOLUTION_INTERVAL': 10,
    'MUTATION_RATE': 0.2,
    'CROSSOVER_RATE': 0.5,
    'ELITISM_COUNT': 20,
    'MAX_CODE_POOL_SIZE': 200,
    'LIBRARY_USAGE_PROBABILITY': 0.8,
    'ML_ENHANCEMENT': True,
    'ML_PREDICTION_THRESHOLD': 0.65,
    'DEEP_LEARNING_ENABLED': True,
    'AUTO_ML_ENABLED': True,
    'QUALITY_THRESHOLD': 75,
    'MIN_FITNESS_FOR_PARENT': 80,
    'MIN_QUALITY_FOR_PARENT': 85,
    'LOW_FITNESS_THRESHOLD': 60,
    'WEAK_CATEGORY_THRESHOLD': 0.3,
    'MAX_ERROR_COUNT': 1,
    'CLEANUP_OLD_GENERATIONS': 10,
    'MAX_LIBRARY_AGE': 15,
    'MAX_FUNCTIONS_PER_LIB': 12,
    'MAX_DUPLICATE_IMPORTS': 0,
    'HEALING_ATTEMPTS': 5,
    'HEALING_PROBABILITY': 0.8,
    'MAX_HEALED_PER_CYCLE': 10,
    'FIX_SYNTAX_AUTO': True,
    'CHECK_FUNCTION_INTEGRITY': True,
    'REMOVE_DEAD_CODE': True,
    'AUTO_MERGE_SIMILAR': True,
    'SIMILARITY_THRESHOLD': 0.85,
    'BALANCE_WEAK_CATEGORIES': True,
    'ENABLE_PROACTIVE_HEALING': True,
    'PARALLEL_PROCESSING': True,
    'CACHE_SIZE': 1000,
    'ASYNC_OPERATIONS': True,
    'DEEP_MUTATION_ENABLED': True,
    'FUNCTION_LEVEL_MUTATION': True,
    'CLASS_LEVEL_MUTATION': True,
    'ARCHITECTURE_EVOLUTION': True,
    'PATTERN_RECOGNITION': True,
    'GENERATIONS_DIR': './generations',
    'BACKUP_DIR': './backups',
    'LIBRARIES_DIR': './evolution_libs',
    'MODELS_DIR': './ml_models',
    'STATE_FILE': './evolution_state.json',
    'LOG_FILE': './evolution.log',
    'REPORTS_DIR': './reports',
    'CODE_POOL_FILE': './code_pool.json',
    'SELF_EVOLUTION_FILE': './self_evolution.py',
    
    # НОВЫЕ НАСТРОЙКИ ДЛЯ УЛУЧШЕНИЙ
    'CODE_COMPACTION_ENABLED': True,
    'COMPACTION_THRESHOLD': 5,  # Поколений без улучшения
    'META_KNOWLEDGE_INJECTION': True,
    'SELF_HEALING_REFACTOR': True,
    'ADAPTIVE_MUTATION_WEIGHTS': True,
    'DYNAMIC_GOAL_CREATION': True,
    'MAX_CUSTOM_GOALS': 10,
    'INNOVATION_THRESHOLD': 0.3,
    'COMPLEXITY_PENALTY': 0.1,
    'HEALTH_WEIGHT': 0.3,
    
    # НОВЫЕ НАСТРОЙКИ ДЛЯ СИНТАКСИЧЕСКОЙ ЧИСТОТЫ
    'ENABLE_PRE_VALIDATION': True,  # Валидация перед сохранением
    'MAX_SYNTAX_ERRORS': 0,  # Ноль синтаксических ошибок
    'AUTO_REJECT_BROKEN_SYNTAX': True,  # Автоматически отклонять код с ошибками
    'ENFORCE_TYPE_HINTS': False,  # Не требовать типы, но поощрять
    'MAX_CONSECUTIVE_FAILURES': 3,  # Максимум неудачных мутаций подряд
}

# ============================================================================
# ДИНАМИЧЕСКИЕ ЦЕЛИ ЭВОЛЮЦИИ
# ============================================================================
BASE_EVOLUTION_GOALS = {
    'ml_ai': {'name': '🤖 ML/AI', 'weight': 3.5, 'icon': '🤖', 'priority': 1, 'unlocked': True, 'category': 'core'},
    'algorithms': {'name': '🔍 Алгоритмы', 'weight': 2.5, 'icon': '🔍', 'priority': 2, 'unlocked': True, 'category': 'core'},
    'integration': {'name': '🔗 Интеграция', 'weight': 2.0, 'icon': '🔗', 'priority': 2, 'unlocked': True, 'category': 'core'},
    'network': {'name': '🌐 Сеть', 'weight': 2.0, 'icon': '🌐', 'priority': 3, 'unlocked': True, 'category': 'core'},
    'database': {'name': '💾 База данных', 'weight': 2.0, 'icon': '💾', 'priority': 3, 'unlocked': True, 'category': 'core'},
    'security': {'name': '🔐 Безопасность', 'weight': 2.0, 'icon': '🔐', 'priority': 3, 'unlocked': True, 'category': 'core'},
    'visualization': {'name': '📊 Визуализация', 'weight': 1.5, 'icon': '📊', 'priority': 4, 'unlocked': True, 'category': 'core'},
    'math': {'name': '🧮 Математика', 'weight': 1.0, 'icon': '🧮', 'priority': 4, 'unlocked': True, 'category': 'core'},
    'strings': {'name': '📝 Текст', 'weight': 1.0, 'icon': '📝', 'priority': 4, 'unlocked': True, 'category': 'core'},
    'files': {'name': '📁 Файлы', 'weight': 1.0, 'icon': '📁', 'priority': 4, 'unlocked': True, 'category': 'core'},
}

LOCKED_GOALS = {
    'quantum': {'name': '⚛️ Квантовые вычисления', 'weight': 5.0, 'icon': '⚛️', 'priority': 0, 
                'unlock_condition': 'ml_ai>0.9&math>0.9', 'category': 'advanced'},
    'blockchain': {'name': '🔗 Блокчейн', 'weight': 4.0, 'icon': '⛓️', 'priority': 0, 
                   'unlock_condition': 'security>0.8&algorithms>0.8', 'category': 'advanced'},
    'evolution': {'name': '🧬 Самоэволюция', 'weight': 10.0, 'icon': '🧬', 'priority': 0, 
                  'unlock_condition': 'meta_evolution>20', 'category': 'meta'},
    'neuro': {'name': '🧠 Нейроморфные вычисления', 'weight': 4.5, 'icon': '🧠', 'priority': 0, 
              'unlock_condition': 'ml_ai>0.85&visualization>0.7', 'category': 'advanced'},
    'robotics': {'name': '🤖 Робототехника', 'weight': 4.0, 'icon': '🦾', 'priority': 0, 
                 'unlock_condition': 'algorithms>0.8&integration>0.8', 'category': 'advanced'},
    'crypto': {'name': '🔐 Криптография', 'weight': 3.5, 'icon': '🔑', 'priority': 0, 
               'unlock_condition': 'security>0.9&math>0.8', 'category': 'advanced'},
}

# Динамические цели, создаваемые системой
CUSTOM_GOALS = {}

EVOLUTION_GOALS = {**BASE_EVOLUTION_GOALS, **{k: v for k, v in LOCKED_GOALS.items() if v.get('unlocked', False)}}

# ============================================================================
# ОПТИМИЗИРОВАННОЕ ЛОГИРОВАНИЕ
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CONFIG['LOG_FILE'], encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# ДЕКОРАТОРЫ ДЛЯ ОПТИМИЗАЦИИ
# ============================================================================
def timed_cache(maxsize=CONFIG['CACHE_SIZE'], seconds=300):
    def wrapper(func):
        cache = {}
        @wraps(func)
        def wrapped(*args, **kwargs):
            key = hashlib.md5(str(args).encode() + str(kwargs).encode()).hexdigest()
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            if len(cache) > maxsize:
                oldest = min(cache.keys(), key=lambda k: cache[k][1])
                del cache[oldest]
            return result
        return wrapped
    return wrapper

def async_operation(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: func(*args, **kwargs))
    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.debug(f"{func.__name__} выполнена за {elapsed:.3f}с")
        return result
    return wrapper

# ============================================================================
# УЛУЧШЕННЫЙ КЛАСС ДЛЯ ПРОВЕРКИ СИНТАКСИСА
# ============================================================================
class SyntaxValidator:
    """Проверяет синтаксис кода до его сохранения."""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.validation_stats = {
                'total_checks': 0,
                'passed': 0,
                'failed': 0,
                'fixed': 0
            }
    
    @measure_time
    def validate_and_fix(self, code: str, auto_fix: bool = True) -> Tuple[bool, Optional[str], List[str]]:
        """
        Проверяет синтаксис и при необходимости исправляет.
        Возвращает (успех, исправленный_код, список_ошибок)
        """
        self.validation_stats['total_checks'] += 1
        errors = []
        
        # Базовая проверка через ast
        try:
            ast.parse(code)
            self.validation_stats['passed'] += 1
            return True, code, errors
        except SyntaxError as e:
            errors.append(str(e))
            self.validation_stats['failed'] += 1
            
            if not auto_fix:
                return False, None, errors
        
        # Пытаемся исправить
        fixed_code = code
        fixed_count = 0
        
        # 1. Исправление незакрытых скобок
        fixed_code, count1 = self._fix_unmatched_braces(fixed_code)
        fixed_count += count1
        
        # 2. Исправление отступов
        fixed_code, count2 = self._fix_indentation(fixed_code)
        fixed_count += count2
        
        # 3. Исправление пропущенных двоеточий
        fixed_code, count3 = self._fix_missing_colons(fixed_code)
        fixed_count += count3
        
        # 4. Исправление пустых тел функций
        fixed_code, count4 = self._fix_empty_bodies(fixed_code)
        fixed_count += count4
        
        # 5. Исправление неправильных операторов
        fixed_code, count5 = self._fix_operators(fixed_code)
        fixed_count += count5
        
        if fixed_count > 0:
            # Проверяем снова
            try:
                ast.parse(fixed_code)
                self.validation_stats['fixed'] += 1
                return True, fixed_code, errors
            except SyntaxError as e2:
                errors.append(str(e2))
                return False, None, errors
        
        return False, None, errors
    
    def _fix_unmatched_braces(self, code: str) -> Tuple[str, int]:
        """Исправляет незакрытые скобки {}, [], ()."""
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        brace_stack = []
        in_string = False
        string_char = ''
        escape = False
        
        for line_num, line in enumerate(lines):
            fixed_line = ''
            for i, char in enumerate(line):
                if not escape:
                    if char in ('"', "'") and (i == 0 or line[i-1] != '\\'):
                        if not in_string:
                            in_string = True
                            string_char = char
                        elif char == string_char:
                            in_string = False
                    elif char == '\\':
                        escape = True
                        fixed_line += char
                        continue
                else:
                    escape = False
                
                if not in_string:
                    if char in '{[(':
                        brace_stack.append((char, line_num, len(fixed_line)))
                    elif char in '}])':
                        if brace_stack:
                            opening, open_line, open_col = brace_stack.pop()
                            expected_close = {'{': '}', '[': ']', '(': ')'}[opening]
                            if char != expected_close:
                                fixed_line += expected_close
                                fixed_count += 1
                                continue
                        else:
                            # Лишняя закрывающая скобка - пропускаем
                            fixed_count += 1
                            continue
                fixed_line += char
            fixed_lines.append(fixed_line)
        
        # Добавляем недостающие закрывающие скобки
        while brace_stack:
            opening, _, _ = brace_stack.pop()
            fixed_lines[-1] += {'{': '}', '[': ']', '(': ')'}[opening]
            fixed_count += 1
        
        return '\n'.join(fixed_lines), fixed_count
    
    def _fix_indentation(self, code: str) -> Tuple[str, int]:
        """Исправляет проблемы с отступами."""
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        indent_levels = [0]
        expected_indent = 0
        
        for i, line in enumerate(lines):
            stripped = line.lstrip()
            if not stripped:
                fixed_lines.append(line)
                continue
            
            current_indent = len(line) - len(stripped)
            is_block_start = stripped.startswith(('def ', 'class ', 'if ', 'for ', 'while ', 'try:', 'with ', 'except', 'finally', 'else:', 'elif '))
            
            if stripped.startswith(('except', 'finally', 'else:', 'elif ')) and len(indent_levels) > 1:
                expected_indent = indent_levels[-2]
            else:
                expected_indent = indent_levels[-1]
            
            if current_indent != expected_indent and stripped:
                # Проверяем, не является ли это концом блока
                if current_indent < expected_indent and i > 0:
                    next_line_stripped = ''
                    if i+1 < len(lines):
                        next_line_stripped = lines[i+1].lstrip()
                    if not next_line_stripped or next_line_stripped.startswith(('def ', 'class ')):
                        if len(indent_levels) > 1:
                            indent_levels.pop()
                        expected_indent = indent_levels[-1]
                        if current_indent != expected_indent:
                            fixed_line = ' ' * expected_indent + stripped
                            fixed_lines.append(fixed_line)
                            fixed_count += 1
                        else:
                            fixed_lines.append(line)
                        continue
                
                fixed_line = ' ' * expected_indent + stripped
                fixed_lines.append(fixed_line)
                fixed_count += 1
            else:
                fixed_lines.append(line)
            
            if is_block_start:
                indent_levels.append(expected_indent + 4)
        
        return '\n'.join(fixed_lines), fixed_count
    
    def _fix_missing_colons(self, code: str) -> Tuple[str, int]:
        """Добавляет пропущенные двоеточия после def, if, for и т.д."""
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        
        keywords = ['def', 'class', 'if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally', 'with']
        
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.endswith(':'):
                for kw in keywords:
                    if stripped.startswith(kw) and '(' in stripped and ')' in stripped:
                        # Проверяем, что это не функция с телом на той же строке
                        if not any(stripped.endswith(x) for x in [':', ' pass', ' return', ' continue', ' break']):
                            line = line + ':'
                            fixed_count += 1
                        break
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines), fixed_count
    
    def _fix_empty_bodies(self, code: str) -> Tuple[str, int]:
        """Добавляет 'pass' в пустые тела функций и классов."""
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            fixed_lines.append(line)
            
            if stripped.startswith(('def ', 'class ')) and stripped.endswith(':'):
                # Проверяем, есть ли тело
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    next_stripped = next_line.lstrip()
                    if not next_stripped or next_stripped.startswith(('def ', 'class ', '@')):
                        # Нет тела, добавляем pass
                        indent = len(line) - len(line.lstrip()) + 4
                        fixed_lines.append(' ' * indent + 'pass')
                        fixed_count += 1
            i += 1
        
        return '\n'.join(fixed_lines), fixed_count
    
    def _fix_operators(self, code: str) -> Tuple[str, int]:
        """Исправляет распространённые ошибки с операторами."""
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        
        for line in lines:
            # Исправляем = вместо == в условиях
            if ' if ' in line and '=' in line and '==' not in line and '!=' not in line and '<=' not in line and '>=' not in line:
                parts = line.split(' if ')
                if len(parts) > 1:
                    condition = parts[1]
                    if '=' in condition and '==' not in condition:
                        # Очень грубое исправление
                        pass
            
            fixed_lines.append(line)
        
        return '\n'.join(fixed_lines), fixed_count
    
    def get_stats(self) -> Dict[str, Any]:
        return dict(self.validation_stats)

# ============================================================================
# УЛУЧШЕННЫЕ КЛАССЫ ДАННЫХ
# ============================================================================
@dataclass
class CodePattern:
    id: str
    code: str
    category: str
    fitness_score: float
    usage_count: int
    success_rate: float
    parent_ids: List[str]
    generation: int
    created_at: str
    complexity: int = 0
    is_elite: bool = False
    uses_libraries: List[str] = field(default_factory=list)
    ml_predictions: Dict[str, float] = field(default_factory=dict)
    last_used: str = ""
    error_count: int = 0
    validation_status: bool = True
    quality_score: float = 100.0
    times_used_as_parent: int = 0
    function_count: int = 0
    class_count: int = 0
    has_duplicates: bool = False
    times_merged: int = 0
    original_id: Optional[str] = None
    performance_score: float = 0.0
    memory_usage: float = 0.0
    execution_time: float = 0.0
    dependencies: List[str] = field(default_factory=list)
    innovation_score: float = 0.0
    evolution_path: List[str] = field(default_factory=list)
    
    # НОВЫЕ ПОЛЯ
    dead_code_removed: int = 0
    last_improvement_gen: int = 0
    stagnation_count: int = 0
    syntax_valid: bool = True  # Всегда true для сохранённых паттернов

@dataclass
class FunctionRecord:
    name: str
    code: str
    category: str
    generation: int
    tests_passed: int
    tests_total: int
    fitness_score: float
    parent_pattern_id: Optional[str]
    created_at: str
    is_active: bool = True
    uses_libraries: List[str] = field(default_factory=list)
    ml_accuracy: float = 0.0
    error_count: int = 0
    validation_status: bool = True
    integrity_check_passed: bool = True
    times_optimized: int = 0
    execution_time: float = 0.0
    call_count: int = 0
    last_called: str = ""
    complexity_score: int = 0
    docstring_quality: float = 1.0

@dataclass
class LibraryRecord:
    name: str
    path: str
    purpose: str
    generation: int
    times_used: int
    tests_passed: int
    tests_total: int
    created_at: str
    fitness_score: float = 0
    exported_functions: List[str] = field(default_factory=list)
    exported_classes: List[str] = field(default_factory=list)
    ml_models: List[str] = field(default_factory=list)
    is_active: bool = True
    error_count: int = 0
    validation_status: bool = True
    health_score: float = 100.0
    last_used_generation: int = 0
    times_used_as_source: int = 0
    duplicate_imports: int = 0
    broken_functions: List[str] = field(default_factory=list)
    healing_attempts: int = 0
    last_healing_attempt: str = ""
    times_healed: int = 0
    times_optimized: int = 0
    dependencies: List[str] = field(default_factory=list)
    size_bytes: int = 0
    lines_of_code: int = 0
    complexity_score: int = 0
    innovation_score: float = 0.0

@dataclass
class MetaEvolutionRecord:
    id: str
    generation: int
    source_libraries: List[str]
    source_functions: List[str]
    new_code: str
    fitness_score: float
    created_at: str
    status: str = "pending"
    validation_status: bool = True
    times_used: int = 0
    architecture_type: str = "standard"
    ml_model_used: Optional[str] = None
    innovation_score: float = 0.0
    
    # НОВЫЕ ПОЛЯ
    successful_combinations: List[Tuple[str, str]] = field(default_factory=list)
    times_injected: int = 0

@dataclass
class SelfEvolutionRecord:
    id: str
    generation: int
    original_code_hash: str
    modified_code: str
    changes: List[str]
    fitness_improvement: float
    created_at: str
    is_active: bool = True

@dataclass
class EvolutionMetrics:
    generation: int
    timestamp: str
    fitness: float
    mutation_rate: float
    crossover_rate: float
    population_size: int
    elite_count: int
    avg_complexity: float
    ml_accuracy: float
    innovation_rate: float
    health_score: float
    performance_score: float

@dataclass
class EvolutionState:
    generation: int = 0
    best_fitness: float = 0
    current_fitness: float = 0
    mutation_count: int = 0
    successful_mutations: int = 0
    failed_mutations: int = 0
    fitness_history: List[float] = field(default_factory=list)
    goals_progress: Dict[str, float] = field(default_factory=dict)
    unlocked_goals: Set[str] = field(default_factory=lambda: set(BASE_EVOLUTION_GOALS.keys()))
    start_time: str = ""
    total_functions: int = 0
    total_classes: int = 0
    code_pool_size: int = 0
    elite_patterns: int = 0
    library_usage_count: int = 0
    ml_models_created: int = 0
    ml_predictions_made: int = 0
    ml_accuracy_avg: float = 0.0
    cross_category_uses: int = 0
    meta_evolution_count: int = 0
    meta_evolution_success: int = 0
    self_evolution_count: int = 0
    self_evolution_success: int = 0
    fixed_syntax_errors: int = 0
    cleaned_libraries: int = 0
    removed_broken_libraries: int = 0
    healed_libraries: int = 0
    added_imports: int = 0
    removed_unused_libraries: int = 0
    avg_health_score: float = 100.0
    removed_duplicate_imports: int = 0
    fixed_broken_functions: int = 0
    removed_dead_code: int = 0
    healing_attempts: int = 0
    successful_healing: int = 0
    balance_adjustments: int = 0
    patterns_merged: int = 0
    functions_optimized: int = 0
    proactive_heals: int = 0
    avg_complexity: float = 0.0
    innovation_score: float = 0.0
    performance_score: float = 0.0
    metrics_history: List[EvolutionMetrics] = field(default_factory=list)
    last_goal: str = "ml_ai"
    created_dependencies: int = 0
    
    # НОВЫЕ ПОЛЯ
    custom_goals_created: int = 0
    meta_injections: int = 0
    compactions_performed: int = 0
    self_healing_refactors: int = 0
    adaptive_weights_applied: int = 0
    stagnation_recovery: int = 0
    mutation_weights: Dict[str, float] = field(default_factory=lambda: {
        'add_feature': 0.25,
        'add_library': 0.20,
        'mutate_code': 0.20,
        'code_compaction': 0.10,
        'self_heal': 0.10,
        'meta_inject': 0.10,
        'create_goal': 0.05
    })
    
    # НОВЫЕ ПОЛЯ ДЛЯ СИНТАКСИЧЕСКОЙ СТАТИСТИКИ
    rejected_syntax_errors: int = 0
    auto_fixed_syntax: int = 0
    consecutive_failures: int = 0
    max_consecutive_failures: int = CONFIG['MAX_CONSECUTIVE_FAILURES']

    def __post_init__(self):
        if not self.goals_progress:
            self.goals_progress = {goal: 0.0 for goal in BASE_EVOLUTION_GOALS.keys()}
        if not self.unlocked_goals:
            self.unlocked_goals = set(BASE_EVOLUTION_GOALS.keys())

# ============================================================================
# НОВЫЙ МОДУЛЬ: СЖАТИЕ И ОПТИМИЗАЦИЯ КОДА (Code Compaction)
# ============================================================================
class CodeCompactor:
    """Сжимает и оптимизирует код, удаляя мёртвые ветки и дубликаты."""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.compaction_stats = {
            'performed': 0,
            'dead_branches_removed': 0,
            'duplicate_lines_removed': 0,
            'redundant_assignments_removed': 0,
            'complexity_reduced': 0
        }
    
    @measure_time
    def compact_code(self, code: str, pattern_id: str = None) -> Tuple[str, Dict[str, int]]:
        """
        Основной метод сжатия кода.
        Возвращает оптимизированный код и статистику изменений.
        """
        stats = {
            'dead_branches': 0,
            'duplicate_lines': 0,
            'redundant_assignments': 0,
            'complexity_reduction': 0
        }
        
        original_lines = code.split('\n')
        original_length = len(original_lines)
        
        # 1. Удаление мёртвых веток (код после return/break/continue)
        code, dead_branches = self._remove_dead_branches(code)
        stats['dead_branches'] = dead_branches
        
        # 2. Объединение идентичных строк
        code, duplicates = self._merge_duplicate_lines(code)
        stats['duplicate_lines'] = duplicates
        
        # 3. Упрощение логики (удаление лишних присваиваний)
        code, redundant = self._simplify_assignments(code)
        stats['redundant_assignments'] = redundant
        
        # 4. Сжатие нескольких except в один
        code = self._compress_except_blocks(code)
        
        # 5. Удаление пустых строк и комментариев (опционально)
        if random.random() < 0.3:  # Не всегда, чтобы не потерять документацию
            code = self._clean_whitespace(code)
        
        # Подсчёт уменьшения сложности
        new_lines = code.split('\n')
        stats['complexity_reduction'] = original_length - len(new_lines)
        
        # Обновляем глобальную статистику
        self.compaction_stats['performed'] += 1
        self.compaction_stats['dead_branches_removed'] += dead_branches
        self.compaction_stats['duplicate_lines_removed'] += duplicates
        self.compaction_stats['redundant_assignments_removed'] += redundant
        self.compaction_stats['complexity_reduced'] += stats['complexity_reduction']
        
        return code, stats
    
    def _remove_dead_branches(self, code: str) -> Tuple[str, int]:
        """Удаляет код после return, break, continue, которые никогда не выполнятся."""
        lines = code.split('\n')
        new_lines = []
        dead_branches = 0
        skip_until_indent = None
        
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Проверяем, не находимся ли мы в режиме пропуска
            if skip_until_indent is not None:
                current_indent = len(line) - len(line.lstrip())
                if current_indent <= skip_until_indent:
                    skip_until_indent = None
                else:
                    dead_branches += 1
                    i += 1
                    continue
            
            # Ищем ключевые слова, после которых код не выполняется
            if any(stripped.startswith(kw) for kw in ['return', 'break', 'continue', 'raise']):
                new_lines.append(line)
                
                # Определяем отступ, до которого нужно пропускать
                current_indent = len(line) - len(line.lstrip())
                skip_until_indent = current_indent
                
                # Проверяем, есть ли на той же строке что-то после ключевого слова
                if stripped.endswith(':'):
                    skip_until_indent = current_indent + 4
            else:
                new_lines.append(line)
            
            i += 1
        
        return '\n'.join(new_lines), dead_branches
    
    def _merge_duplicate_lines(self, code: str) -> Tuple[str, int]:
        """Объединяет идентичные строки кода (кроме импортов и def)."""
        lines = code.split('\n')
        seen_lines = {}
        new_lines = []
        duplicates = 0
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Не трогаем импорты, определения функций и классов
            if stripped.startswith(('import ', 'from ', 'def ', 'class ', '@')):
                new_lines.append(line)
                continue
            
            # Если строка не пустая и не комментарий
            if stripped and not stripped.startswith('#'):
                # Проверяем, была ли такая строка в том же контексте
                context = (stripped, len(line) - len(line.lstrip()))
                if context in seen_lines and seen_lines[context] > i - 10:  # Недавно видели
                    duplicates += 1
                    continue
                seen_lines[context] = i
            
            new_lines.append(line)
        
        return '\n'.join(new_lines), duplicates
    
    def _simplify_assignments(self, code: str) -> Tuple[str, int]:
        """Упрощает цепочки присваиваний."""
        lines = code.split('\n')
        new_lines = []
        redundant = 0
        last_assignment = {}
        
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Ищем присваивания вида "x = something"
            if '=' in stripped and not stripped.startswith(('def ', 'class ', 'import ', 'from ')):
                parts = stripped.split('=', 1)
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    value = parts[1].strip()
                    
                    # Проверяем, не переопределяется ли переменная без использования
                    if var_name in last_assignment:
                        # Проверяем, использовалась ли переменная между присваиваниями
                        used = False
                        for j in range(last_assignment[var_name]['line'] + 1, i):
                            if var_name in lines[j] and '=' not in lines[j].split('=', 1)[0]:
                                used = True
                                break
                        
                        if not used:
                            redundant += 1
                            # Пропускаем это присваивание, оставляем только последнее
                            last_assignment[var_name] = {'line': i, 'value': value}
                            i += 1
                            continue
                    
                    last_assignment[var_name] = {'line': i, 'value': value}
            
            new_lines.append(line)
            i += 1
        
        return '\n'.join(new_lines), redundant
    
    def _compress_except_blocks(self, code: str) -> str:
        """Объединяет несколько except в один, если они делают одно и то же."""
        lines = code.split('\n')
        new_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            if stripped.startswith('except ') and i + 1 < len(lines):
                # Смотрим, что идёт дальше
                next_line = lines[i + 1].strip()
                
                # Если несколько except подряд с одинаковым телом
                exceptions = [stripped]
                body_lines = []
                j = i + 1
                
                # Собираем тело первого except
                indent = len(lines[i + 1]) - len(lines[i + 1].lstrip())
                while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) >= indent):
                    if lines[j].strip():
                        body_lines.append(lines[j])
                    j += 1
                
                # Проверяем следующие except
                k = j
                while k < len(lines) and lines[k].strip().startswith('except '):
                    next_except = lines[k].strip()
                    next_indent = len(lines[k + 1]) - len(lines[k + 1].lstrip()) if k + 1 < len(lines) else 0
                    
                    # Собираем тело следующего except
                    next_body = []
                    l = k + 1
                    while l < len(lines) and (not lines[l].strip() or len(lines[l]) - len(lines[l].lstrip()) >= next_indent):
                        if lines[l].strip():
                            next_body.append(lines[l])
                        l += 1
                    
                    # Если тела одинаковые, объединяем исключения
                    if next_body == body_lines:
                        exc_part = next_except.replace('except ', '').replace(':', '').strip()
                        exceptions.append(exc_part)
                        k = l
                    else:
                        break
                
                if len(exceptions) > 1:
                    # Объединяем все исключения в один except
                    combined = f"except ({', '.join(exceptions)}):"
                    new_lines.append(combined)
                    new_lines.extend(body_lines)
                    i = k
                    continue
            
            new_lines.append(line)
            i += 1
        
        return '\n'.join(new_lines)
    
    def _clean_whitespace(self, code: str) -> str:
        """Удаляет лишние пустые строки и комментарии."""
        lines = code.split('\n')
        new_lines = []
        empty_count = 0
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                empty_count += 1
                if empty_count <= 1:  # Оставляем не больше одной пустой строки подряд
                    new_lines.append(line)
            else:
                empty_count = 0
                if not stripped.startswith('#'):  # Удаляем однострочные комментарии
                    new_lines.append(line)
                elif '"""' in line or "'''" in line:  # Но сохраняем докстринги
                    new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    def get_stats(self) -> Dict[str, Any]:
        return dict(self.compaction_stats)

# ============================================================================
# НОВЫЙ МОДУЛЬ: ВНЕДРЕНИЕ МЕТА-ЗНАНИЙ (ИСПРАВЛЕННЫЙ)
# ============================================================================
class MetaKnowledgeInjector:
    """Внедряет успешные комбинации из мета-эволюции обратно в библиотеки."""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.injection_stats = {
            'performed': 0,
            'hybrid_functions_created': 0,
            'wrappers_created': 0,
            'successful_injections': 0
        }
    
    @measure_time
    def inject_knowledge(self) -> bool:
        """
        Анализирует успешные мета-паттерны и внедряет их знания в обычные библиотеки.
        """
        if not self.evolution.meta_evolution.meta_records:
            return False
        
        # Берём последние успешные мета-паттерны
        successful_meta = [
            r for r in self.evolution.meta_evolution.meta_records.values()
            if r.fitness_score > 85 and r.status == 'success'
        ]
        
        if len(successful_meta) < 2:
            return False
        
        # Анализируем лучший
        best_meta = max(successful_meta, key=lambda r: r.fitness_score)
        
        # Пытаемся извлечь успешные комбинации функций
        combinations = self._extract_function_combinations(best_meta)
        
        if not combinations:
            return False
        
        # Создаём гибридные функции
        created = 0
        for cat1, cat2 in combinations[:3]:  # Не больше 3 за раз
            if self._create_hybrid_function(cat1, cat2, best_meta):
                created += 1
        
        # Создаём функцию-проводник к мета-процессору
        if random.random() < 0.5:
            if self._create_meta_wrapper(best_meta):
                created += 1
        
        if created > 0:
            self.injection_stats['performed'] += 1
            self.injection_stats['successful_injections'] += created
            self.evolution.state.meta_injections += created
        
        return created > 0
    
    def _extract_function_combinations(self, meta_record: MetaEvolutionRecord) -> List[Tuple[str, str]]:
        """Извлекает пары категорий функций, которые часто вызываются вместе."""
        combinations = []
        
        # Анализируем код мета-паттерна
        code = meta_record.new_code
        
        # Ищем вызовы функций из разных библиотек
        libs_used = set()  # Множество для ИМЁН библиотек (строки)
        for lib in self.evolution.library_creator.libraries.values():
            if lib.name in code:
                libs_used.add(lib.name)  # ✅ Добавляем имя, а не объект
        
        # Создаём пары категорий
        lib_list = list(libs_used)
        for i in range(len(lib_list)):
            for j in range(i + 1, len(lib_list)):
                cat1 = self._get_category_from_lib(lib_list[i])
                cat2 = self._get_category_from_lib(lib_list[j])
                if cat1 and cat2 and cat1 != cat2:
                    combinations.append((cat1, cat2))
        
        return list(set(combinations))  # Убираем дубликаты
    
    def _get_category_from_lib(self, lib_name: str) -> Optional[str]:
        """Определяет категорию библиотеки по имени."""
        for cat in EVOLUTION_GOALS.keys():
            if cat in lib_name:
                return cat
        return None
    
    def _create_hybrid_function(self, cat1: str, cat2: str, meta_record: MetaEvolutionRecord) -> bool:
        """Создаёт гибридную функцию, объединяющую две категории."""
        # Находим подходящие функции из каждой категории
        func1 = self._find_best_function(cat1)
        func2 = self._find_best_function(cat2)
        
        if not func1 or not func2:
            return False
        
        # Создаём гибрид
        hybrid_name = f"hybrid_{cat1}_{cat2}_{int(time.time())}"
        hybrid_code = f'''
def {hybrid_name}(data):
    """
    Гибридная функция, объединяющая {cat1} и {cat2}
    Создана на основе мета-эволюции поколения {meta_record.generation}
    """
    try:
        # Шаг 1: применяем функцию из {cat1}
        result1 = {func1.__name__}(data)
        
        # Шаг 2: применяем функцию из {cat2}
        if isinstance(result1, dict) and 'error' in result1:
            return result1
        result2 = {func2.__name__}(result1)
        
        return {{
            'success': True,
            'stage1': result1,
            'stage2': result2,
            'hybrid': True,
            'categories': ['{cat1}', '{cat2}']
        }}
    except Exception as e:
        return {{'success': False, 'error': str(e)}}
'''
        
        # Добавляем импорты
        imports = f"from evolution_libs.{func1.__module__} import {func1.__name__}\n"
        imports += f"from evolution_libs.{func2.__module__} import {func2.__name__}\n"
        
        full_code = imports + hybrid_code
        
        # Проверяем синтаксис через валидатор
        validator = SyntaxValidator()
        is_valid, fixed_code, errors = validator.validate_and_fix(full_code, auto_fix=True)
        if not is_valid:
            return False
        
        # Сохраняем в виде паттерна
        quality = self.evolution.code_analyzer.check_code_quality(fixed_code)
        pattern = CodePattern(
            id=hybrid_name,
            code=fixed_code,
            category='integration',
            fitness_score=85.0,  # Начальное значение
            usage_count=0,
            success_rate=1.0,
            parent_ids=[meta_record.id],
            generation=self.evolution.state.generation,
            created_at=datetime.now().isoformat(),
            complexity=quality['complexity'],
            is_elite=True,  # Сразу делаем элитным
            uses_libraries=[func1.__module__, func2.__module__],
            validation_status=True,
            quality_score=quality['score'],
            innovation_score=0.8,
            syntax_valid=True
        )
        
        self.evolution.code_pool.add_pattern(pattern, self.evolution)
        self.injection_stats['hybrid_functions_created'] += 1
        
        logger.info(f"🔄 ГИБРИД: Создана функция {hybrid_name} из {cat1} + {cat2}")
        return True
    
    def _find_best_function(self, category: str) -> Optional[Any]:
        """Находит лучшую функцию в заданной категории."""
        # Ищем в библиотеках
        for lib in self.evolution.library_creator.libraries.values():
            if category in lib.name and lib.exported_functions:
                try:
                    module = importlib.import_module(f"evolution_libs.{lib.name}")
                    best_func = max(lib.exported_functions, 
                                  key=lambda f: len(getattr(module, f).__code__.co_code) if hasattr(getattr(module, f), '__code__') else 0)
                    return getattr(module, best_func)
                except:
                    pass
        
        # Ищем в пуле паттернов
        patterns = self.evolution.code_pool.get_best_patterns(category, 1)
        if patterns:
            # Создаём временную функцию
            local_ns = {}
            try:
                exec(patterns[0].code, {}, local_ns)
                for name, obj in local_ns.items():
                    if callable(obj) and not name.startswith('_'):
                        return obj
            except:
                pass
        
        return None
    
    def _create_meta_wrapper(self, meta_record: MetaEvolutionRecord) -> bool:
        """Создаёт функцию-обёртку для вызова мета-процессора."""
        # Определяем тип мета-процессора
        if 'EnsembleProcessor' in meta_record.new_code:
            processor_type = 'ensemble'
            processor_name = 'ensemble_processor'
        elif 'HierarchicalProcessor' in meta_record.new_code:
            processor_type = 'hierarchical'
            processor_name = 'hierarchical_processor'
        elif 'PipelineProcessor' in meta_record.new_code:
            processor_type = 'pipeline'
            processor_name = 'pipeline_processor'
        else:
            processor_type = 'standard'
            processor_name = 'meta_processor'
        
        wrapper_name = f"use_{meta_record.id}"
        
        # Экранируем код мета-записи для вставки в строку
        escaped_code = meta_record.new_code.replace('\\', '\\\\').replace("'''", "\\'\\'\\'").replace('"""', '\\"\\"\\"')
        
        wrapper_code = f'''
def {wrapper_name}(data, mode='auto'):
    """
    Обёртка для вызова мета-процессора из поколения {meta_record.generation}
    Тип: {processor_type}
    """
    try:
        # Пытаемся импортировать мета-процессор
        import sys
        import os
        sys.path.insert(0, os.path.dirname(__file__))
        
        # Создаём временный модуль с мета-кодом
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(\"\"\"{escaped_code}\"\"\")
            temp_path = f.name
        
        # Импортируем
        import importlib.util
        spec = importlib.util.spec_from_file_location('meta_module', temp_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Вызываем процессор
        if hasattr(module, '{processor_name}'):
            result = module.{processor_name}(data)
        else:
            # Пробуем найти любой процессор
            for name in dir(module):
                if 'processor' in name.lower() and callable(getattr(module, name)):
                    result = getattr(module, name)(data)
                    break
            else:
                return {{'success': False, 'error': 'Процессор не найден'}}
        
        # Очищаем временный файл
        os.unlink(temp_path)
        
        return {{
            'success': True,
            'result': result,
            'processor_type': '{processor_type}',
            'generation': {meta_record.generation}
        }}
    except Exception as e:
        return {{'success': False, 'error': str(e)}}
'''
        
        # Проверяем синтаксис через валидатор
        validator = SyntaxValidator()
        is_valid, fixed_code, errors = validator.validate_and_fix(wrapper_code, auto_fix=True)
        if not is_valid:
            return False
        
        # Сохраняем
        quality = self.evolution.code_analyzer.check_code_quality(fixed_code)
        pattern = CodePattern(
            id=wrapper_name,
            code=fixed_code,
            category='integration',
            fitness_score=90.0,
            usage_count=0,
            success_rate=1.0,
            parent_ids=[meta_record.id],
            generation=self.evolution.state.generation,
            created_at=datetime.now().isoformat(),
            complexity=quality['complexity'],
            is_elite=True,
            uses_libraries=[],
            validation_status=True,
            quality_score=quality['score'],
            innovation_score=0.9,
            syntax_valid=True
        )
        
        self.evolution.code_pool.add_pattern(pattern, self.evolution)
        self.injection_stats['wrappers_created'] += 1
        
        logger.info(f"🔄 ОБЁРТКА: Создана функция {wrapper_name} для мета-процессора")
        return True
    
    def get_stats(self) -> Dict[str, Any]:
        return dict(self.injection_stats)

# ============================================================================
# УЛУЧШЕННЫЙ МОДУЛЬ: АКТИВНОЕ САМОИСЦЕЛЕНИЕ
# ============================================================================
class AdvancedSelfHealer:
    """Активное самоисцеление с рефакторингом и удалением мёртвого груза."""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.healing_stats = {
            'attempts': 0,
            'successes': 0,
            'dead_code_removed': 0,
            'wrappers_removed': 0,
            'dependencies_restored': 0,
            'refactors_performed': 0
        }
    
    @measure_time
    def heal_pattern(self, pattern: CodePattern) -> Tuple[bool, Optional[CodePattern], List[str]]:
        """
        Пытается исцелить паттерн с помощью продвинутого рефакторинга.
        Возвращает (успех, новый_паттерн, список_изменений)
        """
        self.healing_stats['attempts'] += 1
        changes = []
        
        # 1. Удаление мёртвого груза (неиспользуемые функции)
        code, removed_functions, dead_changes = self._remove_dead_functions(pattern.code)
        if removed_functions > 0:
            changes.extend(dead_changes)
            self.healing_stats['dead_code_removed'] += removed_functions
        
        # 2. Удаление бесполезных обёрток (use_* функции, которые просто вызывают другие)
        code, removed_wrappers, wrapper_changes = self._remove_useless_wrappers(code)
        if removed_wrappers > 0:
            changes.extend(wrapper_changes)
            self.healing_stats['wrappers_removed'] += removed_wrappers
        
        # 3. Восстановление зависимостей
        code, restored_deps, deps_changes = self._restore_dependencies(code, pattern)
        if restored_deps > 0:
            changes.extend(deps_changes)
            self.healing_stats['dependencies_restored'] += restored_deps
        
        # 4. Рефакторинг длинных функций
        code, refactored, refactor_changes = self._refactor_long_functions(code)
        if refactored > 0:
            changes.extend(refactor_changes)
            self.healing_stats['refactors_performed'] += refactored
        
        if not changes:
            return False, None, []
        
        # Проверяем синтаксис через валидатор
        validator = SyntaxValidator()
        is_valid, fixed_code, errors = validator.validate_and_fix(code, auto_fix=True)
        if not is_valid:
            logger.warning(f"❌ Исцеление {pattern.id} нарушило синтаксис")
            return False, None, []
        
        # Создаём новый паттерн
        quality = self.evolution.code_analyzer.check_code_quality(fixed_code)
        new_pattern = CodePattern(
            id=f"{pattern.id}_healed_{int(time.time())}",
            code=fixed_code,
            category=pattern.category,
            fitness_score=pattern.fitness_score * 1.05,  # Бонус за исцеление
            usage_count=pattern.usage_count,
            success_rate=pattern.success_rate,
            parent_ids=pattern.parent_ids + [pattern.id],
            generation=self.evolution.state.generation,
            created_at=datetime.now().isoformat(),
            complexity=quality['complexity'],
            is_elite=pattern.is_elite,
            uses_libraries=pattern.uses_libraries,
            validation_status=True,
            quality_score=quality['score'],
            innovation_score=pattern.innovation_score + 0.1,
            dead_code_removed=removed_functions,
            syntax_valid=True
        )
        
        self.healing_stats['successes'] += 1
        logger.info(f"💊 ИСЦЕЛЕНИЕ: {pattern.id} успешно ({len(changes)} изменений)")
        
        return True, new_pattern, changes
    
    def _remove_dead_functions(self, code: str) -> Tuple[str, int, List[str]]:
        """Удаляет функции, которые определены, но никогда не используются."""
        try:
            tree = ast.parse(code)
            
            # Находим все определённые функции
            defined_functions = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    defined_functions.add(node.name)
            
            # Находим все используемые имена
            used_names = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
            
            # Функции, которые не используются
            dead_functions = defined_functions - used_names
            
            if not dead_functions:
                return code, 0, []
            
            # Удаляем мёртвые функции
            lines = code.split('\n')
            new_lines = []
            skip_until = -1
            removed = 0
            changes = []
            
            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()
                
                if i < skip_until:
                    i += 1
                    continue
                
                # Проверяем, не начало ли это мёртвой функции
                if stripped.startswith('def ') and any(f"def {f}" in stripped for f in dead_functions):
                    func_name = stripped.split('def ')[1].split('(')[0]
                    if func_name in dead_functions:
                        # Пропускаем всю функцию
                        indent = len(line) - len(line.lstrip())
                        j = i + 1
                        while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) > indent):
                            j += 1
                        skip_until = j
                        removed += 1
                        changes.append(f"Удалена мёртвая функция {func_name}")
                        i = j
                        continue
                
                new_lines.append(line)
                i += 1
            
            return '\n'.join(new_lines), removed, changes
        
        except Exception as e:
            logger.debug(f"Ошибка при удалении мёртвых функций: {e}")
            return code, 0, []
    
    def _remove_useless_wrappers(self, code: str) -> Tuple[str, int, List[str]]:
        """Удаляет функции-обёртки вида use_*, которые просто вызывают другие функции."""
        try:
            tree = ast.parse(code)
            
            # Находим все вызовы функций
            calls = {}
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    calls[node.func.id] = calls.get(node.func.id, 0) + 1
            
            lines = code.split('\n')
            new_lines = []
            removed = 0
            changes = []
            skip_until = -1
            
            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()
                
                if i < skip_until:
                    i += 1
                    continue
                
                # Проверяем, не является ли функция бесполезной обёрткой
                if stripped.startswith('def use_') and stripped.endswith(':'):
                    # Анализируем тело функции
                    j = i + 1
                    indent = len(lines[i + 1]) - len(lines[i + 1].lstrip()) if i + 1 < len(lines) else 0
                    body_lines = []
                    while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) >= indent):
                        if lines[j].strip():
                            body_lines.append(lines[j].strip())
                        j += 1
                    
                    # Проверяем, не состоит ли тело только из вызова другой функции
                    if len(body_lines) == 2 and 'try:' in body_lines[0] and 'return' in body_lines[1]:
                        # Простая обёртка
                        removed += 1
                        changes.append(f"Удалена бесполезная обёртка {stripped.split(' ')[1]}")
                        skip_until = j
                        i = j
                        continue
                
                new_lines.append(line)
                i += 1
            
            return '\n'.join(new_lines), removed, changes
        
        except Exception as e:
            logger.debug(f"Ошибка при удалении обёрток: {e}")
            return code, 0, []
    
    def _restore_dependencies(self, code: str, pattern: CodePattern) -> Tuple[str, int, List[str]]:
        """Восстанавливает недостающие импорты зависимостей."""
        try:
            tree = ast.parse(code)
            
            # Находим все используемые имена
            used_names = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
            
            # Находим уже импортированные имена
            imported_names = set()
            existing_imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imported_names.add(alias.name.split('.')[-1])
                        existing_imports.add(f"import {alias.name}")
                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        imported_names.add(alias.name)
                        existing_imports.add(f"from {node.module} import {alias.name}")
            
            # Имена, которые нужно импортировать
            missing_imports = used_names - imported_names - set(dir(__builtins__))
            
            if not missing_imports:
                return code, 0, []
            
            # Пытаемся найти библиотеки, содержащие эти имена
            restored = 0
            changes = []
            imports_to_add = []
            
            for name in missing_imports:
                # Проверяем, есть ли такая функция в пуле паттернов
                found = False
                for p in self.evolution.code_pool.patterns.values():
                    if name in p.code and 'def ' + name in p.code:
                        # Нашли функцию, добавляем импорт
                        imports_to_add.append(f"from evolution_libs.{p.id} import {name}")
                        found = True
                        restored += 1
                        changes.append(f"Добавлен импорт {name} из {p.id}")
                        break
                
                if not found:
                    # Проверяем библиотеки
                    for lib in self.evolution.library_creator.libraries.values():
                        if name in lib.exported_functions:
                            imports_to_add.append(f"from evolution_libs.{lib.name} import {name}")
                            found = True
                            restored += 1
                            changes.append(f"Добавлен импорт {name} из {lib.name}")
                            break
            
            if not imports_to_add:
                return code, 0, []
            
            # Добавляем импорты в начало файла
            lines = code.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith(('import ', 'from ')):
                    insert_pos = i + 1
            
            for imp in imports_to_add:
                lines.insert(insert_pos, imp)
                insert_pos += 1
            
            return '\n'.join(lines), restored, changes
        
        except Exception as e:
            logger.debug(f"Ошибка при восстановлении зависимостей: {e}")
            return code, 0, []
    
    def _refactor_long_functions(self, code: str) -> Tuple[str, int, List[str]]:
        """Разбивает слишком длинные функции на несколько."""
        try:
            tree = ast.parse(code)
            
            lines = code.split('\n')
            new_lines = list(lines)
            refactored = 0
            changes = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Проверяем длину функции
                    if hasattr(node, 'end_lineno') and node.end_lineno - node.lineno > 30:
                        # Слишком длинная функция, нужен рефакторинг
                        func_name = node.name
                        func_body = lines[node.lineno-1:node.end_lineno]
                        
                        # Ищем повторяющиеся блоки
                        blocks = self._extract_repeated_blocks(func_body)
                        
                        if blocks:
                            # Создаём вспомогательные функции
                            helper_funcs = []
                            for i, (block, count) in enumerate(blocks):
                                helper_name = f"_{func_name}_helper_{i}"
                                helper_code = self._create_helper_function(helper_name, block)
                                helper_funcs.append((helper_name, helper_code))
                            
                            # Заменяем блоки вызовами
                            new_func_body = []
                            for line in func_body:
                                replaced = False
                                for helper_name, _ in helper_funcs:
                                    if line.strip() in block:  # Упрощённо
                                        new_func_body.append(f"    {helper_name}(locals())")
                                        replaced = True
                                        break
                                if not replaced:
                                    new_func_body.append(line)
                            
                            # Вставляем вспомогательные функции перед основной
                            insert_pos = node.lineno - 1
                            for _, helper_code in helper_funcs:
                                for h_line in helper_code.split('\n'):
                                    new_lines.insert(insert_pos, h_line)
                                    insert_pos += 1
                            
                            # Обновляем основную функцию
                            new_lines[node.lineno-1:node.end_lineno] = new_func_body
                            
                            refactored += 1
                            changes.append(f"Функция {func_name} разбита на {len(helper_funcs)} helper'ов")
            
            return '\n'.join(new_lines), refactored, changes
        
        except Exception as e:
            logger.debug(f"Ошибка при рефакторинге: {e}")
            return code, 0, []
    
    def _extract_repeated_blocks(self, lines: List[str]) -> List[Tuple[str, int]]:
        """Находит повторяющиеся блоки кода."""
        # Упрощённая реализация
        return []
    
    def _create_helper_function(self, name: str, block_lines: str) -> str:
        """Создаёт вспомогательную функцию из блока кода."""
        return f'''
def {name}(context):
    """Вспомогательная функция, созданная при рефакторинге"""
    {chr(10).join(block_lines)}
'''
    
    def get_stats(self) -> Dict[str, Any]:
        return dict(self.healing_stats)

# ============================================================================
# НОВЫЙ МОДУЛЬ: АДАПТИВНАЯ БАЛАНСИРОВКА
# ============================================================================
class AdaptiveBalancer:
    """Динамически настраивает веса мутаций на основе состояния системы."""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.balance_history = []
        self.last_adjustment = 0
    
    @measure_time
    def adjust_weights(self):
        """Анализирует состояние и корректирует веса мутаций."""
        state = self.evolution.state
        
        # Проверяем, не слишком ли часто балансируем
        if time.time() - self.last_adjustment < 60:  # Не чаще раза в минуту
            return False
        
        changes = {}
        
        # 1. Если здоровье падает, увеличиваем вес исцеления и сжатия
        if state.avg_health_score < 90:
            changes['self_heal'] = state.mutation_weights['self_heal'] * 1.3
            changes['code_compaction'] = state.mutation_weights['code_compaction'] * 1.2
            changes['add_feature'] = state.mutation_weights['add_feature'] * 0.9
            logger.info(f"⚖️ Здоровье низкое ({state.avg_health_score:.1f}), усилено исцеление")
        
        # 2. Если сложность растёт слишком быстро, увеличиваем сжатие
        if state.avg_complexity > 50:
            changes['code_compaction'] = state.mutation_weights['code_compaction'] * 1.4
            changes['add_feature'] = state.mutation_weights['add_feature'] * 0.8
            logger.info(f"⚖️ Сложность высокая ({state.avg_complexity:.1f}), усилено сжатие")
        
        # 3. Если мало инноваций, увеличиваем мета-внедрение
        if state.innovation_score < 0.2:
            changes['meta_inject'] = state.mutation_weights['meta_inject'] * 1.5
            changes['create_goal'] = state.mutation_weights['create_goal'] * 1.3
            logger.info(f"⚖️ Инноваций мало ({state.innovation_score:.2f}), усилена мета-эволюция")
        
        # 4. Если много неиспользуемого кода, усиливаем очистку
        if state.removed_unused_libraries > state.generation * 0.5:  # Эвристика
            changes['self_heal'] = state.mutation_weights['self_heal'] * 1.2
            changes['code_compaction'] = state.mutation_weights['code_compaction'] * 1.2
        
        # 5. Если застой (fitness не растёт), пробуем новые подходы
        if len(state.fitness_history) > 10:
            recent = state.fitness_history[-10:]
            if max(recent) - min(recent) < 100:  # Маленький рост
                changes['meta_inject'] = state.mutation_weights['meta_inject'] * 1.4
                changes['create_goal'] = state.mutation_weights['create_goal'] * 1.4
                changes['add_library'] = state.mutation_weights['add_library'] * 1.2
                state.stagnation_recovery += 1
                logger.info(f"⚖️ Застой, пробуем новые подходы")
        
        if changes:
            # Применяем изменения
            for key, new_value in changes.items():
                if key in state.mutation_weights:
                    state.mutation_weights[key] = new_value
            
            # Нормализуем веса, чтобы сумма осталась 1.0
            total = sum(state.mutation_weights.values())
            for key in state.mutation_weights:
                state.mutation_weights[key] /= total
            
            state.balance_adjustments += 1
            state.adaptive_weights_applied += 1
            self.last_adjustment = time.time()
            
            logger.info(f"⚖️ Новые веса: {state.mutation_weights}")
            return True
        
        return False
    
    def select_mutation_type(self) -> str:
        """
        Выбирает тип мутации на основе текущих весов.
        """
        weights = self.evolution.state.mutation_weights
        return random.choices(
            list(weights.keys()),
            weights=list(weights.values())
        )[0]

# ============================================================================
# НОВЫЙ МОДУЛЬ: ДИНАМИЧЕСКОЕ СОЗДАНИЕ ЦЕЛЕЙ (ИСПРАВЛЕННЫЙ)
# ============================================================================
class DynamicGoalCreator:
    """Создаёт новые цели эволюции на основе текущих потребностей."""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.created_goals = {}
        self.creation_stats = {
            'created': 0,
            'achieved': 0,
            'failed': 0
        }
    
    @measure_time
    def create_new_goal(self) -> Optional[str]:
        """
        Анализирует текущее состояние и создаёт новую цель, если нужно.
        Возвращает ID созданной цели.
        """
        state = self.evolution.state
        
        # Проверяем, не слишком ли много уже созданных целей
        if len(CUSTOM_GOALS) >= CONFIG['MAX_CUSTOM_GOALS']:
            return None
        
        # 1. Анализ узких мест
        weak_spots = self._find_weak_spots()
        if weak_spots:
            return self._create_goal_for_weak_spot(weak_spots[0])
        
        # 2. Анализ комбинаций
        combo_goal = self._create_combinatorial_goal()
        if combo_goal:
            return combo_goal
        
        # 3. Анализ потребностей ML
        ml_goal = self._create_ml_goal()
        if ml_goal:
            return ml_goal
        
        # 4. Анализ производительности
        perf_goal = self._create_performance_goal()
        if perf_goal:
            return perf_goal
        
        return None
    
    def _find_weak_spots(self) -> List[str]:
        """Находит слабые места в системе."""
        weak_spots = []
        state = self.evolution.state
        
        # Проверяем прогресс по основным целям
        for goal, progress in state.goals_progress.items():
            if progress < 0.3:  # Меньше 30%
                weak_spots.append(goal)
        
        # Проверяем категории с низкой инновацией
        for cat in EVOLUTION_GOALS.keys():
            cat_patterns = [p for p in self.evolution.code_pool.patterns.values() if p.category == cat]
            if cat_patterns:
                avg_innovation = sum(p.innovation_score for p in cat_patterns) / len(cat_patterns)
                if avg_innovation < 0.1:
                    weak_spots.append(f"innovate_{cat}")
        
        return weak_spots
    
    def _create_goal_for_weak_spot(self, weak_spot: str) -> Optional[str]:
        """Создаёт цель для усиления слабого места."""
        goal_id = f"strengthen_{weak_spot}_{int(time.time())}"
        
        # Обработка разных типов слабых мест
        if weak_spot.startswith('innovate_'):
            base_cat = weak_spot.replace('innovate_', '')
            # Проверяем, существует ли базовая категория
            if base_cat not in EVOLUTION_GOALS:
                logger.warning(f"Базовая категория {base_cat} не найдена")
                return None
                
            goal_info = {
                'name': f"💡 Инновации в {EVOLUTION_GOALS[base_cat]['name']}",
                'weight': 3.0,
                'icon': '💡',
                'priority': 5,
                'unlocked': True,
                'category': 'dynamic',
                'target': base_cat,
                'condition': f"innovation_{base_cat}>0.3"
            }
        else:
            # Проверяем, существует ли слабое место в целях
            if weak_spot not in EVOLUTION_GOALS:
                # Пробуем найти похожую цель
                found = False
                for goal in EVOLUTION_GOALS:
                    if weak_spot in goal:
                        weak_spot = goal
                        found = True
                        break
                if not found:
                    logger.warning(f"Слабое место {weak_spot} не найдено в целях")
                    return None
                    
            goal_info = {
                'name': f"⚡ Усиление {EVOLUTION_GOALS[weak_spot]['name']}",
                'weight': 2.5,
                'icon': '⚡',
                'priority': 5,
                'unlocked': True,
                'category': 'dynamic',
                'target': weak_spot,
                'condition': f"{weak_spot}>0.6"
            }
        
        # Добавляем в глобальные словари
        CUSTOM_GOALS[goal_id] = goal_info
        self.created_goals[goal_id] = {
            'info': goal_info,
            'created_at': datetime.now().isoformat(),
            'progress': 0.0
        }
        self.creation_stats['created'] += 1
        
        # ВАЖНО: Добавляем в EVOLUTION_GOALS перед использованием
        EVOLUTION_GOALS[goal_id] = goal_info
        
        # Добавляем в состояние
        self.evolution.state.goals_progress[goal_id] = 0.0
        self.evolution.state.unlocked_goals.add(goal_id)
        self.evolution.state.custom_goals_created += 1
        
        logger.info(f"🎯 НОВАЯ ЦЕЛЬ: {goal_info['name']} для усиления {weak_spot}")
        return goal_id
    
    def _create_combinatorial_goal(self) -> Optional[str]:
        """Создаёт цель для комбинирования двух успешных категорий."""
        # Находим пары категорий с высоким прогрессом
        high_progress = [(g, p) for g, p in self.evolution.state.goals_progress.items() if p > 0.8]
        
        if len(high_progress) >= 2:
            # Берём две случайные
            cats = random.sample([g for g, _ in high_progress], 2)
            
            goal_id = f"combine_{cats[0]}_{cats[1]}_{int(time.time())}"
            goal_info = {
                'name': f"🔄 Комбинация {EVOLUTION_GOALS[cats[0]]['name']} + {EVOLUTION_GOALS[cats[1]]['name']}",
                'weight': 4.0,
                'icon': '🔄',
                'priority': 4,
                'unlocked': True,
                'category': 'dynamic',
                'targets': cats,
                'condition': f"hybrid_{cats[0]}_{cats[1]}>0"
            }
            
            CUSTOM_GOALS[goal_id] = goal_info
            self.created_goals[goal_id] = {
                'info': goal_info,
                'created_at': datetime.now().isoformat(),
                'progress': 0.0
            }
            self.creation_stats['created'] += 1
            
            EVOLUTION_GOALS[goal_id] = goal_info
            self.evolution.state.goals_progress[goal_id] = 0.0
            self.evolution.state.unlocked_goals.add(goal_id)
            self.evolution.state.custom_goals_created += 1
            
            logger.info(f"🎯 НОВАЯ ЦЕЛЬ: {goal_info['name']}")
            return goal_id
        
        return None
    
    def _create_ml_goal(self) -> Optional[str]:
        """Создаёт цель для улучшения ML-компонентов."""
        if self.evolution.state.ml_accuracy_avg < 0.7:
            goal_id = f"improve_ml_{int(time.time())}"
            goal_info = {
                'name': f"🤖 Повышение точности ML",
                'weight': 3.5,
                'icon': '🤖',
                'priority': 3,
                'unlocked': True,
                'category': 'dynamic',
                'target': 'ml_ai',
                'condition': 'ml_accuracy>0.8'
            }
            
            CUSTOM_GOALS[goal_id] = goal_info
            self.created_goals[goal_id] = {
                'info': goal_info,
                'created_at': datetime.now().isoformat(),
                'progress': self.evolution.state.ml_accuracy_avg
            }
            self.creation_stats['created'] += 1
            
            EVOLUTION_GOALS[goal_id] = goal_info
            self.evolution.state.goals_progress[goal_id] = self.evolution.state.ml_accuracy_avg
            self.evolution.state.unlocked_goals.add(goal_id)
            self.evolution.state.custom_goals_created += 1
            
            logger.info(f"🎯 НОВАЯ ЦЕЛЬ: {goal_info['name']}")
            return goal_id
        
        return None
    
    def _create_performance_goal(self) -> Optional[str]:
        """Создаёт цель для улучшения производительности."""
        if self.evolution.state.performance_score < 0.5:
            goal_id = f"optimize_perf_{int(time.time())}"
            goal_info = {
                'name': f"⚡ Оптимизация производительности",
                'weight': 3.0,
                'icon': '⚡',
                'priority': 4,
                'unlocked': True,
                'category': 'dynamic',
                'condition': 'performance>0.7'
            }
            
            CUSTOM_GOALS[goal_id] = goal_info
            self.created_goals[goal_id] = {
                'info': goal_info,
                'created_at': datetime.now().isoformat(),
                'progress': self.evolution.state.performance_score
            }
            self.creation_stats['created'] += 1
            
            EVOLUTION_GOALS[goal_id] = goal_info
            self.evolution.state.goals_progress[goal_id] = self.evolution.state.performance_score
            self.evolution.state.unlocked_goals.add(goal_id)
            self.evolution.state.custom_goals_created += 1
            
            logger.info(f"🎯 НОВАЯ ЦЕЛЬ: {goal_info['name']}")
            return goal_id
        
        return None
    
    def update_goal_progress(self, goal_id: str, increment: float):
        """Обновляет прогресс по динамической цели."""
        if goal_id in self.created_goals:
            current = self.evolution.state.goals_progress.get(goal_id, 0)
            new_progress = min(1.0, current + increment)
            self.evolution.state.goals_progress[goal_id] = new_progress
            self.created_goals[goal_id]['progress'] = new_progress
            
            if new_progress >= 1.0 and goal_id not in [g for g, _ in self.evolution.state.unlocked_goals]:
                self.creation_stats['achieved'] += 1
                logger.info(f"🏆 ДОСТИГНУТА ДИНАМИЧЕСКАЯ ЦЕЛЬ: {EVOLUTION_GOALS[goal_id]['name']}")
    
    def get_stats(self) -> Dict[str, Any]:
        return {
            'created': self.creation_stats['created'],
            'achieved': self.creation_stats['achieved'],
            'failed': self.creation_stats['failed'],
            'active': len([g for g, d in self.created_goals.items() if d['progress'] < 1.0])
        }

# ============================================================================
# МОДУЛЬ ДЛЯ ЭВОЛЮЦИИ САМОЙ СИСТЕМЫ (УЛУЧШЕННЫЙ)
# ============================================================================
class SelfEvolutionEngine:
    """Эволюционирует код самой системы"""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.self_records: Dict[str, SelfEvolutionRecord] = {}
        self.last_self_evolution = 0
        self.self_code = self._read_own_code()
        self.self_code_hash = hashlib.md5(self.self_code.encode()).hexdigest()
        
    def _read_own_code(self) -> str:
        """Читает собственный код"""
        try:
            with open(__file__, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Не удалось прочитать собственный код: {e}")
            return ""
    
    def _write_own_code(self, new_code: str) -> bool:
        """Записывает новый код (создаёт резервную копию)"""
        try:
            # Создаём резервную копию
            backup_path = f"{__file__}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(self.self_code)
            
            # Записываем новый код
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(new_code)
            
            logger.info(f"💾 Создана резервная копия: {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Не удалось записать новый код: {e}")
            return False
    
    def should_self_evolve(self) -> bool:
        """Проверяет, нужно ли эволюционировать самой системе"""
        gen = self.evolution.state.generation
        if gen < 10:
            return False
        if gen - self.last_self_evolution >= CONFIG['SELF_EVOLUTION_INTERVAL']:
            return True
        # Эволюционируем, если есть много успешных мета-эволюций
        if self.evolution.state.meta_evolution_success > self.evolution.state.meta_evolution_count * 0.8:
            return random.random() < 0.3
        return False
    
    def evolve_self(self) -> Optional[SelfEvolutionRecord]:
        """Эволюционирует собственный код"""
        logger.info("🧬 САМОЭВОЛЮЦИЯ: Эволюция кода системы...")
        
        improvements = self._analyze_self_code()
        if not improvements:
            logger.info("⚠️ Нет идей для улучшения")
            return None
        
        new_code, changes = self._generate_evolved_code(improvements)
        
        # Проверяем синтаксис через валидатор
        validator = SyntaxValidator()
        is_valid, fixed_code, errors = validator.validate_and_fix(new_code, auto_fix=True)
        if not is_valid:
            logger.error(f"❌ Синтаксическая ошибка в новом коде: {errors}")
            return None
        
        if fixed_code != new_code:
            logger.info(f"🔧 Исправлен синтаксис при самоэволюции")
            new_code = fixed_code
        
        fitness_before = self.evolution.state.best_fitness
        estimated_improvement = self._estimate_improvement(changes)
        
        record_id = f"self_evol_{self.evolution.state.generation}_{int(time.time())}"
        record = SelfEvolutionRecord(
            id=record_id,
            generation=self.evolution.state.generation,
            original_code_hash=self.self_code_hash,
            modified_code=new_code,
            changes=changes,
            fitness_improvement=estimated_improvement,
            created_at=datetime.now().isoformat(),
            is_active=True
        )
        
        self.self_records[record_id] = record
        self.last_self_evolution = self.evolution.state.generation
        self.evolution.state.self_evolution_count += 1
        
        if estimated_improvement > 0:
            self.evolution.state.self_evolution_success += 1
            logger.info(f"✅ САМОЭВОЛЮЦИЯ успешна! Улучшение: +{estimated_improvement:.1f}")
            logger.info(f"📝 Изменения: {', '.join(changes)}")
            
            if self._write_own_code(new_code):
                logger.info("🔄 Новый код системы записан. Требуется перезапуск для полного применения.")
                self.self_code = new_code
                self.self_code_hash = hashlib.md5(new_code.encode()).hexdigest()
        else:
            logger.info(f"⚠️ САМОЭВОЛЮЦИЯ: улучшение незначительное ({estimated_improvement:.1f})")
        
        return record
    
    def _analyze_self_code(self) -> List[Dict]:
        """Анализирует код для поиска мест для улучшения"""
        improvements = []
        
        # Ищем медленные участки
        if 'time.sleep' in self.self_code:
            improvements.append({
                'type': 'performance',
                'target': 'sleep_calls',
                'suggestion': 'Заменить time.sleep на asyncio.sleep для неблокирующих задержек',
                'priority': 0.7
            })
        
        # Ищем устаревшие конструкции
        if 'ThreadPoolExecutor' in self.self_code and 'asyncio' not in self.self_code:
            improvements.append({
                'type': 'modernization',
                'target': 'concurrency',
                'suggestion': 'Добавить асинхронные версии функций',
                'priority': 0.6
            })
        
        # Ищем дублирование кода
        lines = self.self_code.split('\n')
        function_bodies = {}
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and '):' in line:
                func_name = line.split('def ')[1].split('(')[0]
                body = []
                j = i + 1
                indent = len(lines[j]) - len(lines[j].lstrip()) if j < len(lines) else 0
                while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) >= indent):
                    if lines[j].strip():
                        body.append(lines[j].strip())
                    j += 1
                if body:
                    body_str = '\n'.join(body)
                    if body_str in function_bodies:
                        improvements.append({
                            'type': 'refactoring',
                            'target': f'duplicate_{func_name}',
                            'suggestion': f'Функция {func_name} дублирует {function_bodies[body_str]}',
                            'priority': 0.8
                        })
                    else:
                        function_bodies[body_str] = func_name
        
        # Ищем отсутствие типов
        if 'def ' in self.self_code and '->' not in self.self_code:
            improvements.append({
                'type': 'type_hints',
                'target': 'missing_types',
                'suggestion': 'Добавить аннотации типов для лучшей документации',
                'priority': 0.5
            })
        
        # Ищем устаревшие методы
        if '.format(' in self.self_code:
            improvements.append({
                'type': 'modernization',
                'target': 'string_formatting',
                'suggestion': 'Заменить .format() на f-строки для читаемости',
                'priority': 0.4
            })
        
        return improvements
    
    def _generate_evolved_code(self, improvements: List[Dict]) -> Tuple[str, List[str]]:
        """Генерирует эволюционировавший код"""
        new_code = self.self_code
        changes = []
        
        for imp in sorted(improvements, key=lambda x: x['priority'], reverse=True):
            if imp['type'] == 'performance' and imp['target'] == 'sleep_calls':
                lines = new_code.split('\n')
                modified = False
                for i, line in enumerate(lines):
                    if 'time.sleep(' in line and 'async def' in str(lines[max(0, i-5):i]):
                        lines[i] = line.replace('time.sleep', 'await asyncio.sleep')
                        modified = True
                if modified:
                    new_code = '\n'.join(lines)
                    changes.append("Оптимизированы вызовы sleep в асинхронных функциях")
            
            elif imp['type'] == 'type_hints':
                lines = new_code.split('\n')
                modified = False
                for i, line in enumerate(lines):
                    if line.strip().startswith('def ') and '):' in line and '->' not in line:
                        func_name = line.split('def ')[1].split('(')[0]
                        if func_name in ['__init__', '__new__']:
                            continue
                        lines[i] = line.replace('):', ') -> Any:')
                        modified = True
                if modified:
                    has_typing = any('from typing import' in l for l in lines)
                    if not has_typing:
                        for i, line in enumerate(lines):
                            if line.startswith('import ') or line.startswith('from '):
                                lines.insert(i+1, 'from typing import Any')
                                break
                    new_code = '\n'.join(lines)
                    changes.append("Добавлены базовые аннотации типов")
        
        return new_code, changes
    
    def _estimate_improvement(self, changes: List[str]) -> float:
        """Оценивает потенциальное улучшение от изменений"""
        base = 0.0
        for change in changes:
            if 'оптимизир' in change.lower():
                base += 5.0
            elif 'тип' in change.lower():
                base += 2.0
            elif 'рефактор' in change.lower():
                base += 3.0
        return base

# ============================================================================
# МОДУЛЬ ДЛЯ СОЗДАНИЯ НЕДОСТАЮЩИХ ЗАВИСИМОСТЕЙ
# ============================================================================
class DependencyCreator:
    """Создаёт недостающие библиотеки-зависимости"""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.created_deps = set()
        self.dependency_templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, str]:
        """Загружает шаблоны для популярных зависимостей"""
        return {
            'numpy': '''"""
Автоматически созданная заглушка для numpy
"""
import math
from typing import List, Union

class ndarray:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    def __len__(self):
        return len(self.data)

def array(data):
    return ndarray(data)

def zeros(shape):
    if isinstance(shape, int):
        return [0.0] * shape
    return [0.0] * shape[0]

def ones(shape):
    if isinstance(shape, int):
        return [1.0] * shape
    return [1.0] * shape[0]

def mean(arr):
    if hasattr(arr, 'data'):
        arr = arr.data
    return sum(arr) / len(arr)

def std(arr):
    if hasattr(arr, 'data'):
        arr = arr.data
    m = mean(arr)
    return math.sqrt(sum((x - m) ** 2 for x in arr) / len(arr))
''',
            'pandas': '''"""
Автоматически созданная заглушка для pandas
"""
from typing import Dict, List, Any

class DataFrame:
    def __init__(self, data=None):
        self.data = data or {}
        self._series = {}
    
    def __getitem__(self, key):
        return self._series.get(key, [])
    
    def head(self, n=5):
        result = {}
        for k, v in self._series.items():
            result[k] = v[:n]
        return DataFrame(result)
    
    def to_dict(self):
        return self.data

def read_csv(path):
    return DataFrame()

def Series(data):
    return data
''',
            'requests': '''"""
Автоматически созданная заглушка для requests
"""
from typing import Dict, Any

class Response:
    def __init__(self):
        self.status_code = 200
        self.text = ""
        self.headers = {}
    
    def json(self):
        return {}

def get(url, **kwargs):
    return Response()

def post(url, **kwargs):
    return Response()

def put(url, **kwargs):
    return Response()

def delete(url, **kwargs):
    return Response()
''',
            'tensorflow': '''"""
Автоматически созданная заглушка для tensorflow
"""
import random

class keras:
    class layers:
        class Dense:
            def __init__(self, units, activation=None):
                self.units = units
                self.activation = activation
            
            def __call__(self, x):
                return [random.random() for _ in range(self.units)]
    
    class models:
        class Sequential:
            def __init__(self, layers=None):
                self.layers = layers or []
            
            def add(self, layer):
                self.layers.append(layer)
            
            def compile(self, **kwargs):
                pass
            
            def fit(self, x, y, **kwargs):
                return {"history": {"loss": [0.5]}}
            
            def predict(self, x):
                return [random.random()]
''',
            'torch': '''"""
Автоматически созданная заглушка для torch
"""
import random

class Tensor:
    def __init__(self, data):
        self.data = data
    
    def numpy(self):
        return self.data
    
    def to(self, device):
        return self

def tensor(data):
    return Tensor(data)

class nn:
    class Module:
        def __init__(self):
            pass
        
        def forward(self, x):
            return x
        
        def __call__(self, x):
            return self.forward(x)
    
    class Linear(nn.Module):
        def __init__(self, in_features, out_features):
            super().__init__()
            self.in_features = in_features
            self.out_features = out_features
        
        def forward(self, x):
            return [random.random() for _ in range(self.out_features)]
    
    class functional:
        @staticmethod
        def relu(x):
            return [max(0, v) if not isinstance(v, (list, tuple)) else v for v in (x if isinstance(x, list) else [x])]
''',
            'sklearn': '''"""
Автоматически созданная заглушка для sklearn
"""
class ensemble:
    class RandomForestClassifier:
        def __init__(self, **kwargs):
            pass
        
        def fit(self, X, y):
            return self
        
        def predict(self, X):
            return [0] * len(X)
    
    class GradientBoostingClassifier:
        def __init__(self, **kwargs):
            pass
        
        def fit(self, X, y):
            return self
        
        def predict(self, X):
            return [0] * len(X)

class linear_model:
    class LogisticRegression:
        def __init__(self, **kwargs):
            pass
        
        def fit(self, X, y):
            return self
        
        def predict(self, X):
            return [0] * len(X)

class preprocessing:
    class StandardScaler:
        def fit_transform(self, X):
            return X
        
        def transform(self, X):
            return X
''',
            'matplotlib': '''"""
Автоматически созданная заглушка для matplotlib
"""
class pyplot:
    @staticmethod
    def plot(x, y, **kwargs):
        pass
    
    @staticmethod
    def scatter(x, y, **kwargs):
        pass
    
    @staticmethod
    def show():
        pass
    
    @staticmethod
    def savefig(path):
        pass
    
    @staticmethod
    def title(text):
        pass
    
    @staticmethod
    def xlabel(text):
        pass
    
    @staticmethod
    def ylabel(text):
        pass

plt = pyplot()
''',
            'seaborn': '''"""
Автоматически созданная заглушка для seaborn
"""
def set_style(style):
    pass

def heatmap(data, **kwargs):
    pass

def pairplot(data, **kwargs):
    pass
''',
            'evolution_libs': lambda name: f'''"""
Автоматически созданная библиотека {name}
Недостающая зависимость для эволюционной системы
"""
from typing import Any, Dict, List, Optional

__version__ = "1.0.0"
__all__ = ["process", "helper", "utils"]

def process(data: Any) -> Dict[str, Any]:
    """Базовая функция обработки"""
    return {{
        "success": True,
        "data": data,
        "type": type(data).__name__,
        "source": "{name}"
    }}

def helper() -> Dict[str, str]:
    """Вспомогательная функция"""
    return {{
        "name": "{name}",
        "purpose": "Автоматически созданная зависимость"
    }}

def utils() -> Dict[str, Any]:
    """Утилиты"""
    return {{
        "created": "Автоматически",
        "version": __version__
    }}
'''
        }
    
    def ensure_dependency(self, module_name: str) -> bool:
        """Гарантирует наличие зависимости"""
        if module_name in self.created_deps:
            return True
        
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            pass
        
        if module_name.startswith('evolib_'):
            return self._create_evolution_lib(module_name)
        
        return self._create_stub(module_name)
    
    def _create_stub(self, module_name: str) -> bool:
        """Создаёт заглушку для модуля"""
        try:
            lib_path = Path(CONFIG['LIBRARIES_DIR']) / f"{module_name}.py"
            
            if module_name in self.dependency_templates:
                content = self.dependency_templates[module_name]
                if callable(content):
                    content = content(module_name)
            else:
                content = f'''"""
Автоматически созданная заглушка для {module_name}
"""
from typing import Any, Dict, List

__version__ = "0.1.0"

class ModuleStub:
    """Базовая заглушка"""
    
    def __getattr__(self, name):
        return lambda *args, **kwargs: {{
            "success": False,
            "error": f"{module_name}.{{name}} не реализован (заглушка)",
            "stub": True
        }}

def __getattr__(name):
    return getattr(ModuleStub(), name)

# Базовые функции
def version():
    return __version__

def info():
    return {{
        "name": "{module_name}",
        "version": __version__,
        "stub": True,
        "created": "Автоматически эволюционной системой"
    }}
'''
            
            lib_path.write_text(content, encoding='utf-8')
            
            if CONFIG['LIBRARIES_DIR'] not in sys.path:
                sys.path.insert(0, CONFIG['LIBRARIES_DIR'])
            
            logger.info(f"📦 Создана заглушка для {module_name}")
            self.created_deps.add(module_name)
            self.evolution.state.created_dependencies += 1
            return True
            
        except Exception as e:
            logger.error(f"❌ Не удалось создать заглушку для {module_name}: {e}")
            return False
    
    def _create_evolution_lib(self, lib_name: str) -> bool:
        """Создаёт недостающую эволюционную библиотеку"""
        try:
            lib_path = Path(CONFIG['LIBRARIES_DIR']) / f"{lib_name}.py"
            
            category = None
            for cat in EVOLUTION_GOALS.keys():
                if cat in lib_name:
                    category = cat
                    break
            
            if not category:
                category = 'integration'
            
            content = f'''"""
Автоматически восстановленная библиотека {lib_name}
Категория: {category}
Создана: {datetime.now().isoformat()}
"""

from typing import Any, Dict, List, Optional

__version__ = "1.0.0"
__category__ = "{category}"

def process(data: Any) -> Dict[str, Any]:
    """Базовая обработка данных"""
    return {{
        "success": True,
        "data": data,
        "category": "{category}",
        "library": "{lib_name}"
    }}

def get_info() -> Dict[str, Any]:
    """Информация о библиотеке"""
    return {{
        "name": "{lib_name}",
        "category": "{category}",
        "version": __version__,
        "created": "Автоматически восстановлена"
    }}

# Добавляем специфичные функции в зависимости от категории
'''
            
            if category == 'ml_ai':
                content += '''
def predict(data):
    """Заглушка для предсказания"""
    return {"class": "unknown", "confidence": 0.5}

def train(data):
    """Заглушка для обучения"""
    return {"status": "trained", "accuracy": 0.5}
'''
            elif category == 'math':
                content += '''
def calculate(data):
    """Заглушка для вычислений"""
    if isinstance(data, (list, tuple)):
        return {
            "sum": sum(data),
            "mean": sum(data) / len(data) if data else 0,
            "count": len(data)
        }
    return {"value": data}
'''
            elif category == 'algorithms':
                content += '''
def search(data, target):
    """Заглушка для поиска"""
    try:
        if target in data:
            return {"found": True, "index": data.index(target)}
    except:
        pass
    return {"found": False}
'''
            
            lib_path.write_text(content, encoding='utf-8')
            logger.info(f"🔄 Восстановлена библиотека {lib_name}")
            self.created_deps.add(lib_name)
            self.evolution.state.created_dependencies += 1
            return True
            
        except Exception as e:
            logger.error(f"❌ Не удалось восстановить {lib_name}: {e}")
            return False

# ============================================================================
# МОДУЛЬ ДЛЯ РАЗБЛОКИРОВКИ НОВЫХ ЦЕЛЕЙ (УЛУЧШЕННЫЙ)
# ============================================================================
class GoalUnlocker:
    """Разблокирует новые цели при выполнении условий"""
    
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.locked_goals = LOCKED_GOALS.copy()
    
    def check_unlocks(self) -> List[str]:
        """Проверяет, какие цели можно разблокировать"""
        unlocked = []
        
        for goal_id, goal_info in self.locked_goals.items():
            if goal_id in self.evolution.state.unlocked_goals:
                continue
            
            condition = goal_info['unlock_condition']
            if self._check_condition(condition):
                unlocked.append(goal_id)
        
        return unlocked
    
    def _check_condition(self, condition: str) -> bool:
        """Проверяет условие разблокировки"""
        try:
            parts = condition.split('&')
            for part in parts:
                if '>' in part:
                    cat, val = part.split('>')
                    val = float(val)
                    if self.evolution.state.goals_progress.get(cat, 0) <= val:
                        return False
                elif '<' in part:
                    cat, val = part.split('<')
                    val = float(val)
                    if self.evolution.state.goals_progress.get(cat, 0) >= val:
                        return False
                elif '=' in part:
                    cat, val = part.split('=')
                    if cat == 'meta_evolution':
                        if self.evolution.state.meta_evolution_count < int(val):
                            return False
                    elif cat == 'generation':
                        if self.evolution.state.generation < int(val):
                            return False
            return True
        except Exception as e:
            logger.error(f"Ошибка проверки условия {condition}: {e}")
            return False
    
    def unlock_goal(self, goal_id: str) -> bool:
        """Разблокирует новую цель"""
        if goal_id not in self.locked_goals:
            return False
        
        goal_info = self.locked_goals[goal_id]
        
        EVOLUTION_GOALS[goal_id] = {
            'name': goal_info['name'],
            'weight': goal_info['weight'],
            'icon': goal_info['icon'],
            'priority': goal_info['priority'],
            'unlocked': True,
            'category': goal_info.get('category', 'advanced')
        }
        
        self.evolution.state.goals_progress[goal_id] = 0.0
        self.evolution.state.unlocked_goals.add(goal_id)
        
        logger.info(f"🎉 РАЗБЛОКИРОВАНА НОВАЯ ЦЕЛЬ: {goal_info['icon']} {goal_info['name']}")
        return True

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ ИСПРАВИТЕЛЬ СИНТАКСИСА (ИСПОЛЬЗУЕТ НОВЫЙ ВАЛИДАТОР)
# ============================================================================
class SyntaxFixer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.fix_patterns = self._load_fix_patterns()
            self.fix_cache = {}
            self.stats = Counter()
            self.validator = SyntaxValidator()

    def _load_fix_patterns(self) -> Dict[str, List[str]]:
        return {
            'import_duplicate': [
                r'^import\s+(\w+)\s*$',
                r'^from\s+(\w+)\s+import\s+(\w+)\s*$'
            ],
            'missing_imports': [
                'List', 'Dict', 'Any', 'Optional', 'Tuple', 'Union',
                'Callable', 'Set', 'Deque', 'DefaultDict'
            ],
            'broken_functions': [
                r'def\s+(\w+)\s*\([^)]*\)\s*:\s*$',
                r'return\s+[^;]+$'
            ],
            'indentation_errors': [
                r'^(\s+)(?!\s)',
                r':\s*\n\s*([^\s])'
            ]
        }

    @staticmethod
    @lru_cache(maxsize=CONFIG['CACHE_SIZE'])
    def remove_duplicate_imports(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        seen_imports = set()
        fixed_lines = []
        removed = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith(('import ', 'from ')):
                normalized = ' '.join(stripped.split())
                if normalized in seen_imports:
                    removed += 1
                    continue
                seen_imports.add(normalized)
            fixed_lines.append(line)
        return '\n'.join(fixed_lines), removed

    @staticmethod
    @lru_cache(maxsize=CONFIG['CACHE_SIZE'])
    def fix_broken_functions(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        in_function = False
        function_name = ""
        function_lines = []
        function_indent = 0
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if stripped.startswith('def ') and stripped.endswith(':'):
                if function_lines:
                    fixed_func, func_fixed = SyntaxFixer._process_function(
                        function_name, function_lines, function_indent
                    )
                    fixed_lines.extend(fixed_func)
                    fixed_count += func_fixed
                in_function = True
                function_name = stripped[4:].split('(')[0].strip()
                function_indent = len(line) - len(line.lstrip())
                function_lines = [line]
                i += 1
                continue
            if in_function:
                current_indent = len(line) - len(line.lstrip()) if line.strip() else function_indent + 4
                if line.strip() and current_indent <= function_indent:
                    in_function = False
                    fixed_func, func_fixed = SyntaxFixer._process_function(
                        function_name, function_lines, function_indent
                    )
                    fixed_lines.extend(fixed_func)
                    fixed_count += func_fixed
                    function_lines = []
                    continue
                function_lines.append(line)
            else:
                fixed_lines.append(line)
            i += 1
        if function_lines:
            fixed_func, func_fixed = SyntaxFixer._process_function(
                function_name, function_lines, function_indent
            )
            fixed_lines.extend(fixed_func)
            fixed_count += func_fixed
        return '\n'.join(fixed_lines), fixed_count

    @staticmethod
    def _process_function(name: str, lines: List[str], indent: int) -> Tuple[List[str], int]:
        fixed_lines = list(lines)
        fixed_count = 0
        body_lines = lines[1:] if len(lines) > 1 else []
        body_stripped = [l.strip() for l in body_lines if l.strip() and not l.strip().startswith('#')]

        if name == 'sigmoid' and any('return {' in l for l in body_lines):
            fixed_lines = [
                lines[0],
                ' ' * (indent + 4) + '"""Сигмоидная функция активации"""',
                ' ' * (indent + 4) + 'try:',
                ' ' * (indent + 8) + 'return 1 / (1 + math.exp(-x)) if x < 500 else 1',
                ' ' * (indent + 4) + 'except Exception:',
                ' ' * (indent + 8) + 'return 0.5'
            ]
            fixed_count += 1
            return fixed_lines, fixed_count

        if not body_stripped:
            has_docstring = False
            if len(body_lines) >= 1:
                first_line_stripped = body_lines[0].strip()
                if first_line_stripped.startswith('"""') or first_line_stripped.startswith("'''"):
                    has_docstring = True
                    if len(body_lines) == 1:
                        fixed_lines.append(' ' * (indent + 4) + 'pass')
                        fixed_count += 1
                else:
                    fixed_lines.append(' ' * (indent + 4) + 'pass')
                    fixed_count += 1
            else:
                fixed_lines.append(' ' * (indent + 4) + 'pass')
                fixed_count += 1

        if name not in ['__init__', '__new__']:
            has_return = False
            for line in body_lines:
                if 'return' in line and not line.strip().startswith('#'):
                    has_return = True
                    break
            if not has_return:
                if fixed_lines[-1].strip() != 'pass':
                    fixed_lines.append(' ' * (indent + 4) + 'return None')
                else:
                    for i in range(len(fixed_lines)-1, -1, -1):
                        if fixed_lines[i].strip() == 'pass':
                            fixed_lines[i] = ' ' * (indent + 4) + 'return None'
                            break
                fixed_count += 1
        return fixed_lines, fixed_count

    @staticmethod
    @lru_cache(maxsize=CONFIG['CACHE_SIZE'])
    def fix_indentation(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        indent_levels = [0]
        expected_indent = 0

        for i, line in enumerate(lines):
            stripped = line.lstrip()
            if not stripped:
                fixed_lines.append(line)
                continue

            current_indent = len(line) - len(stripped)
            is_block_start = stripped.startswith(('def ', 'class ', 'if ', 'for ', 'while ', 'try:', 'with ', 'except', 'finally', 'else:', 'elif '))

            if stripped.startswith(('except', 'finally', 'else:', 'elif ')) and len(indent_levels) > 1:
                expected_indent = indent_levels[-2]
            else:
                expected_indent = indent_levels[-1]

            if current_indent != expected_indent and stripped:
                if current_indent < expected_indent and i > 0:
                    next_line_stripped = ''
                    if i+1 < len(lines):
                        next_line_stripped = lines[i+1].lstrip()
                    if not next_line_stripped or next_line_stripped.startswith(('def ', 'class ')):
                        if len(indent_levels) > 1:
                            indent_levels.pop()
                        expected_indent = indent_levels[-1]
                        if current_indent != expected_indent:
                            fixed_line = ' ' * expected_indent + stripped
                            fixed_lines.append(fixed_line)
                            fixed_count += 1
                        else:
                            fixed_lines.append(line)
                        continue
                fixed_line = ' ' * expected_indent + stripped
                fixed_lines.append(fixed_line)
                fixed_count += 1
            else:
                fixed_lines.append(line)

            if is_block_start:
                indent_levels.append(expected_indent + 4)

            if i+1 < len(lines):
                next_line = lines[i+1]
                next_stripped = next_line.lstrip()
                if next_stripped:
                    next_indent = len(next_line) - len(next_stripped)
                    if next_indent <= expected_indent and len(indent_levels) > 1:
                        if not next_stripped.startswith(('def ', 'class ')):
                            indent_levels.pop()

        return '\n'.join(fixed_lines), fixed_count

    @staticmethod
    @lru_cache(maxsize=CONFIG['CACHE_SIZE'])
    def fix_all(code: str) -> Tuple[str, int, List[str]]:
        original = code
        total_fixed = 0
        fixes_applied = []
        fix_pipeline = [
            ('remove_duplicate_imports', SyntaxFixer.remove_duplicate_imports),
            ('add_missing_imports', SyntaxFixer._add_missing_imports),
            ('fix_broken_functions', SyntaxFixer.fix_broken_functions),
            ('fix_indentation', SyntaxFixer.fix_indentation),
            ('fix_unmatched_braces', SyntaxFixer._fix_unmatched_braces),
            ('fix_return_outside_function', SyntaxFixer._fix_return_outside_function),
            ('remove_dead_code', SyntaxFixer._remove_dead_code),
            ('optimize_code', SyntaxFixer._optimize_code),
        ]
        for name, fix_func in fix_pipeline:
            try:
                code, count = fix_func(code)
                if count > 0:
                    total_fixed += count
                    fixes_applied.append(f"{name} ({count})")
            except Exception as e:
                logger.debug(f"Ошибка в фиксе {name}: {e}")

        if code != original and total_fixed > 0:
            try:
                ast.parse(code)
                return code, total_fixed, fixes_applied
            except SyntaxError as e:
                logger.debug(f"Не удалось полностью исправить после всех фиксов: {e}")
                return original, 0, []
        return code, total_fixed, fixes_applied

    @staticmethod
    def _add_missing_imports(code: str) -> Tuple[str, int]:
        added = 0
        lines = code.split('\n')
        has_typing = any('from typing import' in line for line in lines)
        needed_types = []
        type_hints = ['List', 'Dict', 'Optional', 'Tuple', 'Union', 'Callable', 'Set', 'Any']
        for type_name in type_hints:
            if type_name in code and not has_typing:
                needed_types.append(type_name)
        if needed_types:
            import_line = f"from typing import {', '.join(needed_types)}"
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith(('import ', 'from ')):
                    insert_pos = i + 1
                elif line.strip() and not line.startswith('#') and insert_pos == i:
                    break
            lines.insert(insert_pos, import_line)
            added = 1
        return '\n'.join(lines), added

    @staticmethod
    def _fix_unmatched_braces(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        brace_stack = []
        in_string = False
        string_char = ''
        escape = False

        for line_num, line in enumerate(lines):
            fixed_line = ''
            for i, char in enumerate(line):
                if not escape:
                    if char in ('"', "'") and (i == 0 or line[i-1] != '\\'):
                        if not in_string:
                            in_string = True
                            string_char = char
                        elif char == string_char:
                            in_string = False
                    elif char == '\\':
                        escape = True
                        fixed_line += char
                        continue
                else:
                    escape = False

                if not in_string:
                    if char in '{[(':
                        brace_stack.append((char, line_num, len(fixed_line)))
                    elif char in '}])':
                        if brace_stack:
                            opening, open_line, open_col = brace_stack.pop()
                            expected_close = {'{': '}', '[': ']', '(': ')'}[opening]
                            if char != expected_close:
                                fixed_line += expected_close
                                fixed_count += 1
                                continue
                        else:
                            fixed_count += 1
                            continue
                fixed_line += char
            fixed_lines.append(fixed_line)

        while brace_stack:
            opening, _, _ = brace_stack.pop()
            fixed_lines[-1] += {'{': '}', '[': ']', '(': ')'}[opening]
            fixed_count += 1

        return '\n'.join(fixed_lines), fixed_count

    @staticmethod
    def _fix_return_outside_function(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        fixed_lines = []
        fixed_count = 0
        in_function = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('def ') and stripped.endswith(':'):
                in_function = True
                fixed_lines.append(line)
            elif stripped.startswith('return ') and not in_function:
                fixed_lines.append('# ' + line + '  # ИСПРАВЛЕНО: return вне функции')
                fixed_count += 1
            else:
                if stripped and not stripped.startswith(('def ', 'class ', '@')):
                    if in_function and not line.startswith(' ' * 4):
                        in_function = False
                fixed_lines.append(line)
        return '\n'.join(fixed_lines), fixed_count

    @staticmethod
    def _remove_dead_code(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        fixed_lines = []
        removed = 0
        try:
            tree = ast.parse(code)
            used_names = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
            for line in lines:
                stripped = line.strip()
                if ' = ' in line and not stripped.startswith('#'):
                    parts = line.split('=')
                    if len(parts) > 0:
                        var_name = parts[0].strip().split()[-1]
                        if var_name.isidentifier() and var_name not in used_names:
                            if var_name not in dir(__builtins__):
                                fixed_lines.append('# ' + line + '  # УДАЛЕНО: неиспользуемая переменная')
                                removed += 1
                                continue
                fixed_lines.append(line)
        except Exception:
            return code, 0
        return '\n'.join(fixed_lines), removed

    @staticmethod
    def _optimize_code(code: str) -> Tuple[str, int]:
        lines = code.split('\n')
        optimized = []
        changes = 0
        for line in lines:
            if '  ' in line and ' = ' not in line:
                line = line.replace('  ', ' ')
                changes += 1
            if line.startswith('from ') and ' import ' in line:
                parts = line.split(' import ')
                if len(parts) == 2 and ',' in parts[1]:
                    imports = [imp.strip() for imp in parts[1].split(',')]
                    if len(imports) > 1:
                        line = f"{parts[0]} import {', '.join(sorted(imports))}"
                        changes += 1
            optimized.append(line)
        return '\n'.join(optimized), changes

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ АНАЛИЗАТОР КОДА (С ВАЛИДАЦИЕЙ)
# ============================================================================
class CodeAnalyzer:
    def __init__(self):
        self.syntax_fixer = SyntaxFixer()
        self.syntax_validator = SyntaxValidator()
        self.analysis_cache = {}
        self.ml_predictor = None
        self.pattern_recognizer = None
        self.dependency_creator = None

    def set_ml_predictor(self, predictor):
        self.ml_predictor = predictor

    def set_pattern_recognizer(self, recognizer):
        self.pattern_recognizer = recognizer
    
    def set_dependency_creator(self, creator):
        self.dependency_creator = creator

    @timed_cache(seconds=60)
    @measure_time
    def calculate_complexity(self, code: str) -> int:
        try:
            tree = ast.parse(code)
            complexity = 1
            for node in ast.walk(tree):
                if isinstance(node, (ast.If, ast.While, ast.For)):
                    complexity += 2
                elif isinstance(node, (ast.Try, ast.ExceptHandler)):
                    complexity += 3
                elif isinstance(node, ast.FunctionDef):
                    complexity += len(node.args.args)
                    complexity += sum(1 for n in ast.walk(node) if isinstance(n, ast.Return))
                elif isinstance(node, ast.ClassDef):
                    complexity += 5
                    complexity += len(node.bases) * 2
                elif isinstance(node, ast.Call):
                    complexity += 1
                elif isinstance(node, (ast.And, ast.Or)):
                    complexity += 1
            return complexity
        except Exception:
            return len([l for l in code.split('\n') if l.strip()])

    @timed_cache(seconds=300)
    @measure_time
    def extract_metadata(self, code: str) -> Dict[str, Any]:
        metadata = {
            'imports': [],
            'functions': [],
            'classes': [],
            'decorators': [],
            'global_vars': [],
            'docstrings': [],
            'line_count': 0,
            'code_lines': 0,
            'comment_lines': 0,
            'blank_lines': 0,
        }
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        metadata['imports'].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        metadata['imports'].append(node.module)
                elif isinstance(node, ast.FunctionDef):
                    metadata['functions'].append({
                        'name': node.name,
                        'args': len(node.args.args),
                        'decorators': [d.id for d in node.decorator_list if hasattr(d, 'id')],
                        'docstring': ast.get_docstring(node) or '',
                        'line_start': node.lineno,
                        'line_end': node.end_lineno,
                    })
                elif isinstance(node, ast.ClassDef):
                    metadata['classes'].append({
                        'name': node.name,
                        'bases': [b.id for b in node.bases if hasattr(b, 'id')],
                        'methods': [n.name for n in node.body if isinstance(n, ast.FunctionDef)],
                        'docstring': ast.get_docstring(node) or '',
                    })
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            metadata['global_vars'].append(target.id)
            lines = code.split('\n')
            metadata['line_count'] = len(lines)
            metadata['blank_lines'] = sum(1 for l in lines if not l.strip())
            metadata['comment_lines'] = sum(1 for l in lines if l.strip().startswith('#'))
            metadata['code_lines'] = metadata['line_count'] - metadata['blank_lines'] - metadata['comment_lines']
        except Exception as e:
            logger.debug(f"Ошибка извлечения метаданных: {e}")
        return metadata

    @measure_time
    def calculate_similarity(self, code1: str, code2: str) -> float:
        if not code1 or not code2:
            return 0.0
        metrics = []
        lines1 = set(code1.split('\n'))
        lines2 = set(code2.split('\n'))
        if lines1 and lines2:
            intersection = lines1.intersection(lines2)
            union = lines1.union(lines2)
            if union:
                metrics.append(len(intersection) / len(union))
        try:
            tree1 = ast.parse(code1)
            tree2 = ast.parse(code2)
            nodes1 = [type(n).__name__ for n in ast.walk(tree1)]
            nodes2 = [type(n).__name__ for n in ast.walk(tree2)]
            common = sum(1 for n in nodes1 if n in nodes2)
            metrics.append(common / max(len(nodes1), len(nodes2), 1))
        except Exception:
            pass
        meta1 = self.extract_metadata(code1)
        meta2 = self.extract_metadata(code2)
        imports_sim = len(set(meta1['imports']) & set(meta2['imports'])) / max(len(set(meta1['imports'] + meta2['imports'])), 1)
        metrics.append(imports_sim)
        funcs1 = {f['name'] for f in meta1['functions']}
        funcs2 = {f['name'] for f in meta2['functions']}
        funcs_sim = len(funcs1 & funcs2) / max(len(funcs1 | funcs2), 1)
        metrics.append(funcs_sim)
        return sum(metrics) / len(metrics) if metrics else 0.0

    @measure_time
    def check_code_quality(self, code: str) -> Dict[str, Any]:
        score = 100
        issues = []
        metadata = self.extract_metadata(code)
        long_lines = 0
        for line in code.split('\n'):
            if len(line) > 100:
                long_lines += 1
        if long_lines > 0:
            penalty = min(20, long_lines * 2)
            score -= penalty
            issues.append(f"Длинные строки: -{penalty}")
        if 'import *' in code:
            score -= 15
            issues.append("import *: -15")
        duplicate_imports = self._count_duplicate_imports(code)
        if duplicate_imports > 0:
            score -= duplicate_imports * 5
            issues.append(f"Дублирующиеся импорты: -{duplicate_imports * 5}")
        if metadata['docstrings']:
            score += min(10, len(metadata['docstrings']) * 2)
        elif len(metadata['functions']) > 0:
            score -= 10
            issues.append("Нет докстрингов: -10")
        if 'except:' in code:
            score -= 20
            issues.append("Голый except: -20")
        elif 'except Exception as e' in code:
            score += 10
        if 'Any' in code and 'from typing import' not in code:
            score -= 5
            issues.append("Нет импорта Any: -5")
        complexity = self.calculate_complexity(code)
        if complexity > 50:
            penalty = (complexity - 50) // 5
            score -= penalty
            issues.append(f"Высокая сложность: -{penalty}")
        if len(metadata['functions']) > CONFIG['MAX_FUNCTIONS_PER_LIB']:
            penalty = (len(metadata['functions']) - CONFIG['MAX_FUNCTIONS_PER_LIB']) * 3
            score -= penalty
            issues.append(f"Много функций: -{penalty}")
        is_ml = self._is_ml_code(code)
        if is_ml:
            score += 15
        return {
            'score': max(0, min(100, score)),
            'complexity': complexity,
            'lines': metadata['line_count'],
            'code_lines': metadata['code_lines'],
            'comment_lines': metadata['comment_lines'],
            'blank_lines': metadata['blank_lines'],
            'function_count': len(metadata['functions']),
            'class_count': len(metadata['classes']),
            'import_count': len(metadata['imports']),
            'long_lines': long_lines,
            'duplicate_imports': duplicate_imports,
            'has_docstring': len(metadata['docstrings']) > 0,
            'is_ml_code': is_ml,
            'issues': issues,
            'metadata': metadata
        }

    def _count_duplicate_imports(self, code: str) -> int:
        lines = code.split('\n')
        seen = set()
        duplicates = 0
        for line in lines:
            stripped = line.strip()
            if stripped.startswith(('import ', 'from ')):
                normalized = ' '.join(stripped.split())
                if normalized in seen:
                    duplicates += 1
                seen.add(normalized)
        return duplicates

    def _is_ml_code(self, code: str) -> bool:
        ml_keywords = [
            'neural', 'network', 'train', 'predict', 'classifier',
            'accuracy', 'sigmoid', 'weights', 'activation', 'model',
            'deep', 'learning', 'ai', 'intelligence', 'gradient',
            'tensor', 'layer', 'epoch', 'batch', 'loss', 'optimizer',
            'backpropagation', 'convolution', 'pooling', 'dropout'
        ]
        code_lower = code.lower()
        return any(kw in code_lower for kw in ml_keywords)

    @measure_time
    def validate_syntax(self, code: str, auto_fix: bool = True) -> Tuple[bool, Optional[str], Optional[str], List[str]]:
        """Проверяет синтаксис кода, используя новый валидатор."""
        is_valid, fixed_code, errors = self.syntax_validator.validate_and_fix(code, auto_fix)
        
        if is_valid:
            if fixed_code != code:
                return True, f"Исправлено {len(errors)} ошибок", fixed_code, errors
            return True, None, code, errors
        else:
            return False, errors[0] if errors else "Неизвестная ошибка", code, errors

    def predict_quality(self, code: str) -> float:
        if self.ml_predictor:
            return self.ml_predictor.predict_code_quality(code)
        quality = self.check_code_quality(code)
        return quality['score'] / 100

    def validate_library_health(self, code: str) -> Dict[str, Any]:
        health = {
            'is_valid': False,
            'syntax_errors': [],
            'quality_score': 0,
            'has_functions': False,
            'function_count': 0,
            'import_issues': [],
            'can_import': False,
            'recommend_action': 'keep',
            'duplicate_imports': 0,
            'broken_functions': []
        }
        is_valid, error_msg, fixed_code, errors = self.validate_syntax(code, auto_fix=True)
        health['is_valid'] = is_valid
        health['syntax_errors'] = errors
        if not is_valid:
            health['recommend_action'] = 'delete'
            return health
        quality = self.check_code_quality(code)
        health['quality_score'] = quality['score']
        health['duplicate_imports'] = quality.get('duplicate_imports', 0)
        health['broken_functions'] = quality.get('broken_functions', [])
        health['function_count'] = quality.get('function_count', 0)
        functions = self.extract_metadata(code)['functions']
        health['has_functions'] = len(functions) > 0
        if not health['has_functions']:
            health['recommend_action'] = 'delete'
            return health
        imports = self.extract_metadata(code)['imports']
        for imp in imports:
            if imp not in sys.modules and not imp.startswith('evolution_libs'):
                try:
                    importlib.import_module(imp)
                except ImportError:
                    health['import_issues'].append(f"Не найден модуль: {imp}")
                    
                    if self.dependency_creator:
                        if self.dependency_creator.ensure_dependency(imp):
                            health['import_issues'].remove(f"Не найден модуль: {imp}")
                            health['import_issues'].append(f"Создана заглушка: {imp}")
        
        if len(health['import_issues']) > 2:
            health['recommend_action'] = 'delete'
        elif quality['score'] < 50:
            health['recommend_action'] = 'delete'
        elif len(health['broken_functions']) > 0:
            health['recommend_action'] = 'fix'
        elif health['duplicate_imports'] > CONFIG['MAX_DUPLICATE_IMPORTS']:
            health['recommend_action'] = 'fix'
        elif health['function_count'] > CONFIG['MAX_FUNCTIONS_PER_LIB']:
            health['recommend_action'] = 'optimize'
        else:
            health['recommend_action'] = 'keep'
        try:
            ast.parse(code)
            health['can_import'] = True
        except:
            health['can_import'] = False
        return health

class PatternRecognizer:
    def __init__(self):
        self.patterns = self._load_patterns()
        self.pattern_cache = {}

    def _load_patterns(self) -> Dict[str, Dict]:
        return {
            'singleton': {
                'pattern': r'class\s+\w+.*?_instance\s*=\s*None.*?__new__',
                'weight': 0.8
            },
            'factory': {
                'pattern': r'def\s+create_\w+.*?return\s+\w+\(',
                'weight': 0.7
            },
            'observer': {
                'pattern': r'def\s+notify.*?def\s+update',
                'weight': 0.6
            },
            'decorator': {
                'pattern': r'@\w+\s*def',
                'weight': 0.5
            },
            'ml_model': {
                'pattern': r'class\s+\w+Model.*?def\s+(train|predict)',
                'weight': 1.0
            },
            'data_pipeline': {
                'pattern': r'def\s+(preprocess|transform|normalize)',
                'weight': 0.6
            }
        }

    def recognize(self, code: str) -> List[Dict[str, Any]]:
        found = []
        for name, pattern_info in self.patterns.items():
            import re
            if re.search(pattern_info['pattern'], code, re.MULTILINE | re.DOTALL):
                found.append({
                    'name': name,
                    'weight': pattern_info['weight'],
                    'confidence': self._calculate_confidence(code, name)
                })
        return found

    def _calculate_confidence(self, code: str, pattern: str) -> float:
        confidence = 0.5
        occurrences = code.lower().count(pattern.lower())
        confidence += min(0.3, occurrences * 0.1)
        if pattern == 'ml_model' and ('import numpy' in code or 'import tensorflow' in code):
            confidence += 0.2
        return min(1.0, confidence)

# ============================================================================
# УЛУЧШЕННЫЙ ML ПРЕДСКАЗАТЕЛЬ
# ============================================================================
class MLPredictor:
    def __init__(self, evolution_system=None):
        self.evolution = evolution_system
        self.models = {}
        self.predictions = []
        self.accuracy = 0.7
        self.training_data = []
        self.model_cache = {}
        self.performance_history = []
        self._initialize_models()

    def _initialize_models(self):
        self.models = {
            'quality_predictor': self._create_quality_model(),
            'success_predictor': self._create_success_model(),
            'pattern_predictor': self._create_pattern_model(),
            'innovation_predictor': self._create_innovation_model()
        }

    def _create_quality_model(self):
        return {
            'weights': self._initialize_weights(10),
            'bias': 0.5,
            'learning_rate': 0.01
        }

    def _create_success_model(self):
        return {
            'weights': self._initialize_weights(8),
            'bias': 0.5,
            'learning_rate': 0.01
        }

    def _create_pattern_model(self):
        return {
            'patterns': self._extract_patterns() if self.evolution else [],
            'weights': [1.0] * 5
        }

    def _create_innovation_model(self):
        return {
            'weights': self._initialize_weights(6),
            'threshold': 0.7
        }

    def _initialize_weights(self, size: int) -> List[float]:
        return [random.uniform(-0.1, 0.1) for _ in range(size)]

    def _extract_patterns(self) -> List[Dict]:
        if not self.evolution or not hasattr(self.evolution, 'meta_evolution'):
            return []
        patterns = []
        if hasattr(self.evolution.meta_evolution, 'meta_records'):
            for record in list(self.evolution.meta_evolution.meta_records.values())[-20:]:
                if record.fitness_score > 80:
                    patterns.append({
                        'code': record.new_code[:200],
                        'fitness': record.fitness_score
                    })
        return patterns

    def set_evolution_system(self, evolution_system):
        self.evolution = evolution_system
        self.models['pattern_predictor']['patterns'] = self._extract_patterns()

    def predict_mutation_success(self, code: str, category: str) -> float:
        heuristic = self._heuristic_prediction(code, category)
        ml_score = self._ml_prediction(code, category)
        combined = 0.4 * heuristic + 0.6 * ml_score
        if self.performance_history:
            recent = self.performance_history[-10:]
            avg_performance = sum(recent) / len(recent) if recent else 0.5
            combined = 0.7 * combined + 0.3 * avg_performance
        if self.evolution:
            self.evolution.state.ml_predictions_made += 1
        return min(1.0, max(0.0, combined))

    def _heuristic_prediction(self, code: str, category: str) -> float:
        score = 0.5
        try:
            ast.parse(code)
            score += 0.2
        except:
            score -= 0.2
        if '"""' in code or "'''" in code:
            score += 0.1
        category_keywords = {
            'ml_ai': ['neural', 'train', 'predict', 'model', 'learning'],
            'math': ['sum', 'mean', 'median', 'calculate', 'stat'],
            'algorithms': ['search', 'sort', 'find', 'binary', 'quick'],
            'integration': ['connect', 'bridge', 'adapt', 'convert']
        }
        if category in category_keywords:
            matches = sum(1 for kw in category_keywords[category] if kw in code.lower())
            score += matches * 0.05
        if 'except:' in code:
            score -= 0.15
        if 'import *' in code:
            score -= 0.1
        if len(code.split('\n')) > 200:
            score -= 0.1
        return max(0.0, min(1.0, score))

    def _ml_prediction(self, code: str, category: str) -> float:
        features = self._extract_features(code, category)
        model = self.models['success_predictor']
        activation = sum(f * w for f, w in zip(features, model['weights'])) + model['bias']
        prediction = 1 / (1 + math.exp(-activation))
        return prediction

    def _extract_features(self, code: str, category: str) -> List[float]:
        features = []
        features.append(min(1.0, len(code) / 5000))
        features.append(min(1.0, len(code.split('\n')) / 100))
        features.append(1.0 if 'class ' in code else 0.0)
        features.append(min(1.0, code.count('def ') / 20))
        ml_keywords = ['neural', 'train', 'predict', 'model']
        ml_count = sum(code.lower().count(kw) for kw in ml_keywords)
        features.append(min(1.0, ml_count / 10))
        for cat in EVOLUTION_GOALS.keys():
            features.append(1.0 if cat == category else 0.0)
        return features

    def predict_code_quality(self, code: str) -> float:
        features = self._extract_quality_features(code)
        model = self.models['quality_predictor']
        activation = sum(f * w for f, w in zip(features, model['weights'])) + model['bias']
        quality = 1 / (1 + math.exp(-activation))
        return quality

    def _extract_quality_features(self, code: str) -> List[float]:
        features = []
        lines = code.split('\n')
        avg_line_length = sum(len(l) for l in lines) / max(1, len(lines))
        features.append(min(1.0, avg_line_length / 80))
        comment_lines = sum(1 for l in lines if l.strip().startswith('#'))
        comment_ratio = comment_lines / max(1, len(lines))
        features.append(comment_ratio)
        imports = sum(1 for l in lines if l.startswith(('import ', 'from ')))
        features.append(min(1.0, imports / 10))
        has_docstrings = 1.0 if '"""' in code or "'''" in code else 0.0
        features.append(has_docstrings)
        try:
            tree = ast.parse(code)
            complexity = sum(1 for _ in ast.walk(tree)) / 100
            features.append(min(1.0, complexity))
        except:
            features.append(0.5)
        return features

    def update_model(self, features: List[float], actual_success: bool):
        model = self.models['success_predictor']
        prediction = sum(f * w for f, w in zip(features, model['weights'])) + model['bias']
        target = 1.0 if actual_success else 0.0
        error = target - (1 / (1 + math.exp(-prediction)))
        for i in range(len(model['weights'])):
            gradient = error * features[i]
            model['weights'][i] += model['learning_rate'] * gradient
        model['bias'] += model['learning_rate'] * error
        self.performance_history.append(1.0 if actual_success else 0.0)
        if len(self.performance_history) > 100:
            self.performance_history.pop(0)
        self.accuracy = sum(self.performance_history) / len(self.performance_history) if self.performance_history else 0.7

    def predict_innovation(self, code: str) -> float:
        model = self.models['innovation_predictor']
        features = [
            min(1.0, len(set(code.split())) / 100),
            1.0 if any(c.isupper() for c in code) else 0.0,
            code.count('lambda') / 10,
            1.0 if 'yield' in code else 0.0,
            1.0 if 'async' in code or 'await' in code else 0.0,
            code.count('@') / 5
        ]
        innovation = sum(f * w for f, w in zip(features, model['weights']))
        return min(1.0, innovation / model['threshold'])

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ МЕНЕДЖЕР ПАМЯТИ
# ============================================================================
class MemoryManager:
    def __init__(self, max_cache_size=CONFIG['CACHE_SIZE']):
        self.max_cache_size = max_cache_size
        self.cache = {}
        self.access_times = {}
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            self.access_times[key] = time.time()
            self.hits += 1
            return self.cache[key]
        self.misses += 1
        return None

    def set(self, key: str, value: Any):
        if len(self.cache) >= self.max_cache_size:
            self._cleanup()
        self.cache[key] = value
        self.access_times[key] = time.time()

    def _cleanup(self):
        if len(self.cache) < self.max_cache_size:
            return
        sorted_keys = sorted(self.access_times.keys(), key=lambda k: self.access_times[k])
        to_remove = sorted_keys[:len(self.cache) // 4]
        for key in to_remove:
            if key in self.cache:
                del self.cache[key]
            if key in self.access_times:
                del self.access_times[key]

    def get_stats(self) -> Dict[str, Any]:
        total = self.hits + self.misses
        return {
            'size': len(self.cache),
            'max_size': self.max_cache_size,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': self.hits / max(1, total)
        }

    def clear(self):
        self.cache.clear()
        self.access_times.clear()
        gc.collect()

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ ГЕНЕТИЧЕСКИЙ ПУЛ (УЛУЧШЕННЫЙ С ВАЛИДАЦИЕЙ)
# ============================================================================
class GeneticCodePool:
    def __init__(self, max_size: int = CONFIG['MAX_CODE_POOL_SIZE']):
        self.max_size = max_size
        self.patterns: Dict[str, CodePattern] = {}
        self.elite_patterns: List[str] = []
        self.pattern_by_category: Dict[str, List[str]] = defaultdict(list)
        self.code_analyzer = None
        self.mutation_history = []
        self.crossover_history = []
        self.lock = threading.RLock()
        self.pool_stats = {
            'adds': 0,
            'removes': 0,
            'merges': 0,
            'elite_promotions': 0,
            'rejected_syntax': 0
        }
        
        # НОВЫЕ ПОЛЯ
        self.stagnant_patterns: List[str] = []
        self.compactor = None
        self.healer = None
        self.syntax_validator = SyntaxValidator()

    def set_code_analyzer(self, analyzer):
        self.code_analyzer = analyzer
    
    def set_compactor(self, compactor):
        self.compactor = compactor
    
    def set_healer(self, healer):
        self.healer = healer

    def load_pool(self):
        if Path(CONFIG['CODE_POOL_FILE']).exists():
            try:
                with open(CONFIG['CODE_POOL_FILE'], 'r', encoding='utf-8') as f:
                    data = json.load(f)
                with self.lock:
                    for p in data.get('patterns', []):
                        for field in ['performance_score', 'memory_usage', 'execution_time',
                                      'dependencies', 'innovation_score', 'evolution_path',
                                      'dead_code_removed', 'last_improvement_gen', 'stagnation_count',
                                      'syntax_valid']:
                            if field not in p:
                                if field == 'syntax_valid':
                                    p[field] = True
                                elif field in ['dependencies', 'evolution_path']:
                                    p[field] = []
                                else:
                                    p[field] = 0.0
                        pattern = CodePattern(**p)
                        self.patterns[pattern.id] = pattern
                        self.pattern_by_category[pattern.category].append(pattern.id)
                        if pattern.is_elite:
                            self.elite_patterns.append(pattern.id)
                logger.info(f"📦 Загружено {len(self.patterns)} паттернов")
            except Exception as e:
                logger.error(f"Ошибка загрузки пула: {e}")

    def save_pool(self):
        try:
            with self.lock:
                data = {
                    'last_updated': datetime.now().isoformat(),
                    'patterns': [asdict(p) for p in self.patterns.values()],
                    'stats': self.pool_stats
                }
                with open(CONFIG['CODE_POOL_FILE'], 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Ошибка сохранения пула: {e}")

    def add_pattern(self, pattern: CodePattern, evolution_system=None) -> bool:
        with self.lock:
            # Сначала проверяем синтаксис
            is_valid, fixed_code, errors = self.syntax_validator.validate_and_fix(
                pattern.code, auto_fix=CONFIG['FIX_SYNTAX_AUTO']
            )
            
            if not is_valid and CONFIG['AUTO_REJECT_BROKEN_SYNTAX']:
                self.pool_stats['rejected_syntax'] += 1
                logger.warning(f"❌ Паттерн {pattern.id} отклонён из-за синтаксических ошибок: {errors}")
                if evolution_system:
                    evolution_system.state.rejected_syntax_errors += 1
                return False
            
            if fixed_code != pattern.code:
                logger.info(f"🔧 Исправлен синтаксис паттерна {pattern.id}")
                pattern.code = fixed_code
                if evolution_system:
                    evolution_system.state.auto_fixed_syntax += 1
            
            pattern.syntax_valid = True
            
            for existing in self.patterns.values():
                if existing.code == pattern.code:
                    existing.usage_count += 1
                    existing.last_used = datetime.now().isoformat()
                    return False
            
            # Проверяем на застой
            if evolution_system:
                gen_diff = evolution_system.state.generation - pattern.generation
                if gen_diff > CONFIG['COMPACTION_THRESHOLD'] and pattern.fitness_score < 90:
                    pattern.stagnation_count += 1
                    if pattern.stagnation_count > 3 and pattern.id not in self.stagnant_patterns:
                        self.stagnant_patterns.append(pattern.id)
            
            if CONFIG['AUTO_MERGE_SIMILAR'] and self.code_analyzer:
                for pid, existing in list(self.patterns.items()):
                    if (existing.category == pattern.category and
                            existing.fitness_score > 70 and
                            pattern.fitness_score > 70):
                        similarity = self.code_analyzer.calculate_similarity(existing.code, pattern.code)
                        if similarity > CONFIG['SIMILARITY_THRESHOLD']:
                            logger.info(f"🔗 Слияние паттернов: {existing.id} и {pattern.id}")
                            self._merge_patterns(existing, pattern)
                            self.pool_stats['merges'] += 1
                            if evolution_system:
                                evolution_system.state.patterns_merged += 1
                            return True
            
            if pattern.quality_score < CONFIG['QUALITY_THRESHOLD'] and not pattern.is_elite:
                logger.debug(f"Паттерн {pattern.id} не добавлен (качество: {pattern.quality_score:.0f})")
                return False
            
            if pattern.id in self.patterns:
                old = self.patterns[pattern.id]
                if pattern.fitness_score > old.fitness_score:
                    self.patterns[pattern.id] = pattern
                    return True
            
            if len(self.patterns) >= self.max_size:
                self._remove_worst()
            
            pattern.last_used = datetime.now().isoformat()
            self.patterns[pattern.id] = pattern
            self.pattern_by_category[pattern.category].append(pattern.id)
            self.pool_stats['adds'] += 1
            
            if pattern.fitness_score >= 90 and pattern.quality_score >= 90:
                pattern.is_elite = True
                if pattern.id not in self.elite_patterns:
                    self.elite_patterns.append(pattern.id)
                    self.pool_stats['elite_promotions'] += 1
            return True

    def _merge_patterns(self, pattern1: CodePattern, pattern2: CodePattern):
        pattern1.times_merged += 1
        pattern2.times_merged += 1
        pattern2.original_id = pattern1.id
        pattern1.usage_count += pattern2.usage_count
        pattern1.times_used_as_parent += pattern2.times_used_as_parent
        pattern1.fitness_score = max(pattern1.fitness_score, pattern2.fitness_score)
        if len(pattern2.code) > len(pattern1.code):
            pattern1.code = pattern2.code

    def _remove_worst(self):
        candidates = [p for p in self.patterns.values() if not p.is_elite]
        if not candidates:
            return
        now = datetime.now()
        for p in candidates:
            age = 0
            if p.created_at:
                try:
                    created = datetime.fromisoformat(p.created_at)
                    age = (now - created).days * 24 * 60 + (now - created).seconds / 60
                except:
                    pass
            p.combined_score = (
                    p.fitness_score * 0.3 +
                    p.quality_score * 0.2 +
                    p.times_used_as_parent * 5 -
                    p.error_count * 10 -
                    age * 0.1 -
                    (10 if p.has_duplicates else 0) +
                    (5 if p.times_merged > 0 else 0) +
                    p.innovation_score * 20 -
                    p.stagnation_count * 5
            )
        to_remove = sorted(candidates, key=lambda x: x.combined_score)[:max(1, len(candidates) // 5)]
        for p in to_remove:
            if p.id in self.elite_patterns:
                self.elite_patterns.remove(p.id)
            if p.id in self.pattern_by_category.get(p.category, []):
                self.pattern_by_category[p.category].remove(p.id)
            if p.id in self.stagnant_patterns:
                self.stagnant_patterns.remove(p.id)
            del self.patterns[p.id]
            self.pool_stats['removes'] += 1

    def select_parent(self, category: str, min_quality: float = 80.0) -> Optional[CodePattern]:
        with self.lock:
            candidates = []
            for pid in self.pattern_by_category.get(category, []):
                p = self.patterns.get(pid)
                if (p and p.fitness_score >= min_quality and
                        p.error_count < CONFIG['MAX_ERROR_COUNT'] and
                        p.validation_status and
                        p.quality_score >= CONFIG['MIN_QUALITY_FOR_PARENT'] and
                        not p.has_duplicates and
                        p.stagnation_count < 3 and
                        p.syntax_valid):  # Только синтаксически валидные
                    candidates.append(p)
            if not candidates:
                candidates = [p for p in self.patterns.values()
                              if p.fitness_score >= min_quality and
                              p.error_count < CONFIG['MAX_ERROR_COUNT'] and
                              p.validation_status and
                              p.quality_score >= CONFIG['MIN_QUALITY_FOR_PARENT'] - 10 and
                              not p.has_duplicates and
                              p.stagnation_count < 5 and
                              p.syntax_valid]
            if not candidates:
                return None
            tournament_size = min(3, len(candidates))
            tournament = random.sample(candidates, tournament_size)
            selected = max(tournament, key=lambda p: (
                    p.fitness_score * 0.4 +
                    p.quality_score * 0.3 +
                    p.times_used_as_parent * 2 +
                    p.innovation_score * 10 -
                    p.stagnation_count * 2
            ))
            selected.usage_count += 1
            selected.times_used_as_parent += 1
            selected.last_used = datetime.now().isoformat()
            return selected

    def crossover(self, parent1: CodePattern, parent2: CodePattern) -> Tuple[str, List[str]]:
        code1_lines = parent1.code.split('\n')
        code2_lines = parent2.code.split('\n')
        start1 = next((i for i, l in enumerate(code1_lines) if 'def ' in l or 'class ' in l), 0)
        start2 = next((i for i, l in enumerate(code2_lines) if 'def ' in l or 'class ' in l), 0)
        header = code1_lines[:start1] if parent1.fitness_score >= parent2.fitness_score else code2_lines[:start2]
        body1 = code1_lines[start1:]
        body2 = code2_lines[start2:]
        imports = set()
        for line in body1 + body2:
            if line.startswith(('import ', 'from ')):
                imports.add(line)
        if len(body1) > 5 and len(body2) > 5:
            point1 = self._find_good_crossover_point(body1)
            point2 = self._find_good_crossover_point(body2)
            child_body = body1[:point1] + body2[point2:]
        else:
            child_body = []
            for i in range(max(len(body1), len(body2))):
                if i < len(body1) and (i % 2 == 0 or i >= len(body2)):
                    child_body.append(body1[i])
                if i < len(body2) and (i % 2 == 1 or i >= len(body1)):
                    child_body.append(body2[i])
        child_code = '\n'.join(header + list(imports) + [''] + child_body)
        self.crossover_history.append({
            'parents': [parent1.id, parent2.id],
            'timestamp': datetime.now().isoformat()
        })
        return child_code, [parent1.id, parent2.id]

    def _find_good_crossover_point(self, lines: List[str]) -> int:
        if len(lines) < 10:
            return random.randint(2, len(lines) - 3) if len(lines) > 4 else random.randint(1, max(1, len(lines)-1))
        function_ends = []
        for i, line in enumerate(lines):
            if i > 0 and line.strip() and not line.startswith(' ') and lines[i - 1].strip():
                function_ends.append(i)
        if function_ends:
            return random.choice(function_ends)
        return random.randint(2, len(lines) - 3)

    def mutate(self, code: str, mutation_rate: float = 0.15) -> str:
        lines = code.split('\n')
        mutated = []
        has_docstring = any('"""' in line or "'''" in line for line in lines)
        has_type_hints = any('->' in line for line in lines)
        for i, line in enumerate(lines):
            should_mutate = random.random() < mutation_rate
            if should_mutate and line.strip() and not line.strip().startswith('#'):
                mutation_type = random.choices(
                    ['space', 'comment', 'improve', 'docstring', 'type_hint',
                     'optimize', 'refactor', 'add_error_handling'],
                    weights=[0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1]
                )[0]
                if mutation_type == 'space' and ' = ' in line:
                    line = line.replace(' = ', '  =  ', 1)
                elif mutation_type == 'comment' and 'return' in line:
                    line = line + '  # evolved'
                elif mutation_type == 'improve':
                    line = self._improve_line(line)
                elif mutation_type == 'type_hint' and 'def ' in line and '->' not in line:
                    line = self._add_type_hint(line)
                elif mutation_type == 'optimize':
                    line = self._optimize_line(line)
                elif mutation_type == 'refactor':
                    line = self._refactor_line(line)
                elif mutation_type == 'add_error_handling':
                    line = self._add_error_handling(line)
            mutated.append(line)
        if not has_docstring and random.random() < 0.3:
            mutated = self._add_docstring(mutated)
        result = '\n'.join(mutated)
        try:
            ast.parse(result)
            return result
        except SyntaxError:
            return code

    def _improve_line(self, line: str) -> str:
        improvements = [
            ('if not data', 'if data is None or len(data) == 0'),
            ('except:', 'except Exception as e:'),
            ('return None', 'return None  # no result'),
            ('for i in range(len(', 'for i, item in enumerate('),
        ]
        for old, new in improvements:
            if old in line:
                line = line.replace(old, new)
                break
        return line

    def _add_type_hint(self, line: str) -> str:
        if '(' in line and ')' in line:
            parts = line.split('(')
            if len(parts) > 1:
                func_name = parts[0].replace('def ', '').strip()
                return f"def {func_name}(*args, **kwargs) -> Any:"
        return line

    def _optimize_line(self, line: str) -> str:
        if '  ' in line:
            line = line.replace('  ', ' ')
        line = line.replace(' == True', '')
        line = line.replace(' == False', ' not ')
        return line

    def _refactor_line(self, line: str) -> str:
        if 'lambda' in line and len(line) < 50:
            pass
        return line

    def _add_error_handling(self, line: str) -> str:
        if '[' in line and ']' in line and 'return' in line:
            line = line.replace('return', 'try:\nreturn') + '\nexcept IndexError:\nreturn None'
        return line

    def _add_docstring(self, lines: List[str]) -> List[str]:
        for i, line in enumerate(lines):
            if 'def ' in line:
                func_name = line.split('def ')[1].split('(')[0]
                indent = len(line) - len(line.lstrip())
                docstring = f'{" " * (indent + 4)}"""Функция {func_name}"""'
                lines.insert(i + 1, docstring)
                break
        return lines

    def get_best_patterns(self, category: str, count: int = 3, min_quality: float = 85.0) -> List[CodePattern]:
        with self.lock:
            candidates = []
            for pid in self.pattern_by_category.get(category, []):
                p = self.patterns.get(pid)
                if (p and p.error_count < CONFIG['MAX_ERROR_COUNT'] and
                        p.validation_status and
                        p.quality_score >= min_quality and
                        not p.has_duplicates and
                        p.stagnation_count < 3 and
                        p.syntax_valid):
                    candidates.append(p)
            candidates.sort(key=lambda p: (
                    p.fitness_score * 0.4 +
                    p.quality_score * 0.3 +
                    p.innovation_score * 0.3 -
                    p.stagnation_count * 0.1
            ), reverse=True)
            return candidates[:count]

    def get_elite_patterns(self, count: int = CONFIG['ELITISM_COUNT']) -> List[CodePattern]:
        with self.lock:
            elite = []
            for eid in self.elite_patterns[:count]:
                if eid in self.patterns:
                    p = self.patterns[eid]
                    if (p.error_count < CONFIG['MAX_ERROR_COUNT'] and
                            p.validation_status and
                            not p.has_duplicates and
                            p.syntax_valid):
                        elite.append(p)
            elite.sort(key=lambda p: p.fitness_score, reverse=True)
            return elite[:count]

    def get_stagnant_patterns(self, count: int = 5) -> List[CodePattern]:
        """Возвращает застойные паттерны для обработки."""
        with self.lock:
            stagnant = []
            for sid in self.stagnant_patterns[:count]:
                if sid in self.patterns:
                    p = self.patterns[sid]
                    if p.syntax_valid:
                        stagnant.append(p)
            return stagnant

    def mark_improved(self, pattern_id: str):
        """Отмечает, что паттерн был улучшен."""
        if pattern_id in self.patterns:
            self.patterns[pattern_id].stagnation_count = 0
            self.patterns[pattern_id].last_improvement_gen = self.patterns[pattern_id].generation
            if pattern_id in self.stagnant_patterns:
                self.stagnant_patterns.remove(pattern_id)

    def cleanup_old_patterns(self, max_age_minutes: int = CONFIG['CLEANUP_OLD_GENERATIONS'] * 5) -> int:
        now = datetime.now()
        to_remove = []
        with self.lock:
            for pid, pattern in self.patterns.items():
                if pattern.is_elite:
                    continue
                if pattern.last_used:
                    try:
                        last_used = datetime.fromisoformat(pattern.last_used)
                        age_minutes = (now - last_used).total_seconds() / 60
                        if age_minutes > max_age_minutes and pattern.times_used_as_parent < 1:
                            to_remove.append(pid)
                    except:
                        pass
            for pid in to_remove:
                if pid in self.elite_patterns:
                    self.elite_patterns.remove(pid)
                if pid in self.pattern_by_category.get(self.patterns[pid].category, []):
                    self.pattern_by_category[self.patterns[pid].category].remove(pid)
                if pid in self.stagnant_patterns:
                    self.stagnant_patterns.remove(pid)
                del self.patterns[pid]
            if to_remove:
                logger.info(f"🧹 Очищено {len(to_remove)} старых паттернов")
                self.pool_stats['removes'] += len(to_remove)
            return len(to_remove)

    def get_stats(self) -> Dict[str, Any]:
        with self.lock:
            categories = {}
            for cat in EVOLUTION_GOALS.keys():
                cat_patterns = [p for p in self.patterns.values() if p.category == cat]
                if cat_patterns:
                    categories[cat] = {
                        'count': len(cat_patterns),
                        'avg_fitness': sum(p.fitness_score for p in cat_patterns) / len(cat_patterns),
                        'elite_count': sum(1 for p in cat_patterns if p.is_elite),
                        'stagnant_count': sum(1 for p in cat_patterns if p.id in self.stagnant_patterns)
                    }
            return {
                'size': len(self.patterns),
                'elite_count': len(self.elite_patterns),
                'stagnant_count': len(self.stagnant_patterns),
                'categories': categories,
                'pool_stats': self.pool_stats,
                'mutation_history': len(self.mutation_history),
                'crossover_history': len(self.crossover_history)
            }

# ============================================================================
# УЛУЧШЕННЫЙ META-ЭВОЛЮЦИОННЫЙ ДВИЖОК
# ============================================================================
class MetaEvolutionEngine:
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.meta_records: Dict[str, MetaEvolutionRecord] = {}
        self.last_meta_generation = 0
        self.architecture_patterns = {}
        self.innovation_tracker: Dict[str, int] = defaultdict(int)
        self.meta_stats = {
            'total': 0,
            'success': 0,
            'innovations': 0,
            'avg_fitness': 0
        }
        self.syntax_validator = SyntaxValidator()

    def should_trigger_meta_evolution(self) -> bool:
        gen = self.evolution.state.generation
        if gen < 5:
            return False
        if gen - self.last_meta_generation >= CONFIG['META_EVOLUTION_INTERVAL']:
            return True
        if random.random() < self._calculate_innovation_probability():
            return True
        return False

    def _calculate_innovation_probability(self) -> float:
        if len(self.meta_records) < 5:
            return 0.3
        recent = list(self.meta_records.values())[-5:]
        avg_fitness = sum(r.fitness_score for r in recent) / len(recent) if recent else 0
        if avg_fitness > 90:
            return 0.4
        elif avg_fitness < 70:
            return 0.2
        return 0.3

    def create_meta_evolution(self) -> Optional[MetaEvolutionRecord]:
        logger.info("🚀 META-EVOLUTION: Глубокая эволюция...")
        source_libs = self._select_source_libraries()
        if len(source_libs) < 2:
            logger.info(f"⚠️ Недостаточно библиотек: {len(source_libs)}")
            return None
        architecture = self._select_architecture(source_libs)
        new_code = self._generate_advanced_meta_code(source_libs, architecture)
        
        # Проверяем синтаксис через валидатор
        is_valid, fixed_code, errors = self.syntax_validator.validate_and_fix(new_code, auto_fix=True)
        if not is_valid:
            logger.error(f"❌ Ошибка синтаксиса в meta-коде: {errors}")
            return None
        if fixed_code != new_code:
            logger.info(f"🔧 Исправлен синтаксис meta-кода")
            self.evolution.state.fixed_syntax_errors += 1
            new_code = fixed_code
        
        quality = self.evolution.code_analyzer.check_code_quality(new_code)
        fitness = self._evaluate_meta_code(new_code, source_libs, quality, architecture)
        
        # Запоминаем успешные комбинации
        successful_combinations = []
        if fitness > 80:
            for i, lib1 in enumerate(source_libs):
                for j, lib2 in enumerate(source_libs[i+1:], i+1):
                    successful_combinations.append((lib1.name, lib2.name))
        
        meta_id = f"meta_{self.evolution.state.generation}_{int(time.time())}"
        record = MetaEvolutionRecord(
            id=meta_id,
            generation=self.evolution.state.generation,
            source_libraries=[lib.name for lib in source_libs],
            source_functions=[],
            new_code=new_code,
            fitness_score=fitness,
            created_at=datetime.now().isoformat(),
            status="success" if fitness > 75 else "partial",
            validation_status=True,
            times_used=0,
            architecture_type=architecture,
            ml_model_used=self._get_best_ml_model(),
            innovation_score=self._calculate_innovation_score(new_code, source_libs),
            successful_combinations=successful_combinations,
            times_injected=0
        )
        self.meta_records[meta_id] = record
        self.last_meta_generation = self.evolution.state.generation
        self.evolution.state.meta_evolution_count += 1
        self.meta_stats['total'] += 1
        if fitness > 75:
            self.evolution.state.meta_evolution_success += 1
            self.meta_stats['success'] += 1
            logger.info(f"✅ META-EVOLUTION успешен: {fitness:.0f}")
            pattern = CodePattern(
                id=meta_id,
                code=new_code,
                category='integration',
                fitness_score=fitness,
                usage_count=0,
                success_rate=1.0,
                parent_ids=[],
                generation=self.evolution.state.generation,
                created_at=datetime.now().isoformat(),
                complexity=quality['complexity'],
                is_elite=fitness > 90,
                uses_libraries=[lib.name for lib in source_libs],
                validation_status=True,
                quality_score=quality['score'],
                innovation_score=record.innovation_score,
                syntax_valid=True
            )
            self.evolution.code_pool.add_pattern(pattern, self.evolution)
        else:
            logger.info(f"⚠️ META-EVOLUTION частичный: {fitness:.0f}")
        return record

    def _select_source_libraries(self) -> List[LibraryRecord]:
        candidates = []
        for lib in self.evolution.library_creator.libraries.values():
            if not lib.is_active:
                continue
            score = (
                    lib.fitness_score * 0.3 +
                    lib.health_score * 0.2 +
                    lib.times_used_as_source * 2 +
                    len(lib.exported_functions) * 5 +
                    (10 if lib.ml_models else 0) +
                    (5 if lib.times_healed < 2 else 0)
            )
            if lib.duplicate_imports <= CONFIG['MAX_DUPLICATE_IMPORTS']:
                candidates.append((lib, score))
        candidates.sort(key=lambda x: x[1], reverse=True)
        top_libs = [lib for lib, _ in candidates[:5]]
        if len(top_libs) < 2:
            return []
        k = random.randint(2, min(4, len(top_libs)))
        return random.sample(top_libs, k)

    def _select_architecture(self, libs: List[LibraryRecord]) -> str:
        architectures = [
            'standard',
            'pipeline',
            'ensemble',
            'hierarchical',
            'adaptive',
            'distributed'
        ]
        has_ml = any(lib.ml_models for lib in libs)
        has_math = any('math' in lib.name for lib in libs)
        has_integration = any('integration' in lib.name for lib in libs)
        if has_ml and has_math:
            return 'ensemble'
        elif has_ml:
            return 'pipeline'
        elif has_integration:
            return 'hierarchical'
        return random.choice(architectures[:3])

    def _get_best_ml_model(self) -> Optional[str]:
        ml_libs = self.evolution.library_creator.get_ml_libraries()
        if ml_libs:
            best = max(ml_libs, key=lambda l: l.fitness_score)
            if best.ml_models:
                return f"{best.name}.{best.ml_models[0]}"
        return None

    def _generate_advanced_meta_code(self, libs: List[LibraryRecord], architecture: str) -> str:
        gen = self.evolution.state.generation
        imports = set()
        imports.add("from typing import Any, Dict, Optional, List, Union, Callable, TypeVar, Generic")
        lib_imports = []
        for lib in libs:
            imports.add(f"from evolution_libs.{lib.name} import *")
            lib_imports.append(lib.name)
            lib.times_used_as_source += 1
        if architecture == 'ensemble':
            code = self._generate_ensemble_code(gen, lib_imports)
        elif architecture == 'pipeline':
            code = self._generate_pipeline_code(gen, lib_imports)
        elif architecture == 'hierarchical':
            code = self._generate_hierarchical_code(gen, lib_imports)
        else:
            code = self._generate_standard_meta_code(gen, lib_imports)
        import_section = '\n'.join(sorted(imports)) + '\n'
        return import_section + code

    def _generate_standard_meta_code(self, gen: int, libs: List[str]) -> str:
        libs_str = ', '.join(libs[:3]) if libs else 'none'
        return f'''"""
META-EVOLUTION v2.0 | Поколение: {gen}
Архитектура: Стандартная
Источники: {libs_str}
"""
__version__ = f"meta.{gen}.0"
__meta_type__ = "standard"
import time
import json
import inspect
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, Optional, List, Union, Callable, TypeVar, Generic

T = TypeVar('T')

class MetaProcessor:
    def __init__(self, max_workers: int = 4):
        self.libraries = {{}}
        self.functions = {{}}
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.stats = {{
            'calls': 0,
            'successes': 0,
            'errors': 0,
            'parallel_calls': 0,
            'avg_response_time': 0,
            'start_time': time.time()
        }}
        self.cache = {{}}
        self._load_components()

    def _load_components(self):
        import importlib
        libs_dir = './evolution_libs'
        if os.path.exists(libs_dir):
            for file in os.listdir(libs_dir):
                if file.endswith('.py') and file.startswith('evolib_'):
                    lib_name = file[:-3]
                    try:
                        spec = importlib.util.spec_from_file_location(lib_name, f'{{libs_dir}}/{{file}}')
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            self.libraries[lib_name] = module
                            for name, obj in inspect.getmembers(module):
                                if inspect.isfunction(obj) and not name.startswith('_'):
                                    self.functions[f"{{lib_name}}.{{name}}"] = obj
                    except Exception as e:
                        print(f"Ошибка загрузки {{lib_name}}: {{e}}")

    def process(self, data: Any, strategy: str = 'auto', parallel: bool = False) -> Dict[str, Any]:
        start = time.time()
        self.stats['calls'] += 1
        if data is None:
            return {{
                'success': False,
                'error': 'No data provided',
                'stats': self.stats
            }}
        result = {{
            'input_type': type(data).__name__,
            'strategy': strategy,
            'generation': {gen},
            'outputs': {{}},
            'timestamp': time.time()
        }}
        try:
            if parallel and len(self.functions) > 1:
                futures = []
                for name, func in list(self.functions.items())[:5]:
                    future = self.executor.submit(self._safe_call, func, data)
                    futures.append((name, future))
                for name, future in futures:
                    try:
                        result['outputs'][name] = future.result(timeout=2)
                    except Exception as e:
                        result['outputs'][name] = {{'error': str(e)}}
                self.stats['parallel_calls'] += 1
            else:
                if strategy in ('auto', 'ml'):
                    ml_result = self._apply_ml(data)
                    if ml_result:
                        result['outputs']['ml'] = ml_result
                if strategy in ('auto', 'math'):
                    math_result = self._apply_math(data)
                    if math_result:
                        result['outputs']['math'] = math_result
                if strategy == 'all':
                    for name, func in list(self.functions.items())[:5]:
                        result['outputs'][name] = self._safe_call(func, data)
            result['success'] = True
            self.stats['successes'] += 1
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
            self.stats['errors'] += 1
        elapsed = time.time() - start
        self.stats['avg_response_time'] = (
            self.stats['avg_response_time'] * (self.stats['calls'] - 1) + elapsed
        ) / self.stats['calls']
        return result

    def _safe_call(self, func: Callable, data: Any) -> Any:
        try:
            return func(data)
        except Exception as e:
            return {{'error': str(e)}}

    def _apply_ml(self, data):
        results = {{}}
        for name, func in self.functions.items():
            if any(x in name.lower() for x in ['predict', 'classify', 'neural', 'ml']):
                try:
                    results[name] = func(data)
                except Exception:
                    pass
        return results if results else None

    def _apply_math(self, data):
        if isinstance(data, (list, tuple)) and data:
            try:
                import statistics
                return {{
                    'sum': sum(data),
                    'mean': statistics.mean(data) if len(data) > 1 else data[0],
                    'median': statistics.median(data) if len(data) > 1 else data[0],
                    'len': len(data),
                    'min': min(data),
                    'max': max(data),
                    'std': statistics.stdev(data) if len(data) > 1 else 0
                }}
            except Exception:
                pass
        return None

    def clear_cache(self):
        self.cache.clear()

    def get_stats(self) -> Dict[str, Any]:
        return dict(self.stats)

def meta_processor(data, mode='auto', parallel=False):
    processor = MetaProcessor()
    return processor.process(data, mode, parallel)
'''

    def _generate_ensemble_code(self, gen: int, libs: List[str]) -> str:
        libs_str = ', '.join(libs[:3]) if libs else 'none'
        return f'''"""
META-EVOLUTION v2.0 | Поколение: {gen}
Архитектура: Ансамблевая
Источники: {libs_str}
"""
__version__ = f"meta.{gen}.0"
__meta_type__ = "ensemble"
import time
import json
import inspect
import os
import asyncio
from collections import Counter
from typing import List, Dict, Any, Optional

class EnsembleProcessor:
    def __init__(self):
        self.models = {{}}
        self.weights = {{}}
        self.stats = {{
            'calls': 0,
            'successes': 0,
            'errors': 0,
            'consensus_rate': 0,
            'start_time': time.time()
        }}
        self._load_models()

    def _load_models(self):
        import importlib
        libs_dir = './evolution_libs'
        if os.path.exists(libs_dir):
            for file in os.listdir(libs_dir):
                if file.endswith('.py') and file.startswith('evolib_'):
                    lib_name = file[:-3]
                    try:
                        spec = importlib.util.spec_from_file_location(lib_name, f'{{libs_dir}}/{{file}}')
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            for name, obj in inspect.getmembers(module):
                                if inspect.isclass(obj) and any(
                                        x in name.lower() for x in ['neural', 'network', 'model', 'classifier']
                                ):
                                    self.models[f"{{lib_name}}.{{name}}"] = obj
                                    self.weights[f"{{lib_name}}.{{name}}"] = 1.0
                    except Exception as e:
                        print(f"Ошибка загрузки {{lib_name}}: {{e}}")

    def process(self, data: Any, strategy: str = 'voting') -> Dict[str, Any]:
        self.stats['calls'] += 1
        if data is None:
            return {{
                'success': False,
                'error': 'No data provided',
                'stats': self.stats
            }}
        result = {{
            'input_type': type(data).__name__,
            'strategy': strategy,
            'generation': {gen},
            'predictions': {{}},
            'voting_result': None,
            'confidence': 0,
            'timestamp': time.time()
        }}
        try:
            predictions = []
            weights = []
            for name, model_class in self.models.items():
                try:
                    model = model_class()
                    if hasattr(model, 'predict'):
                        pred = model.predict(data)
                    elif hasattr(model, 'classify'):
                        pred = model.classify(data)
                    else:
                        continue
                    result['predictions'][name] = pred
                    predictions.append(str(pred))
                    weights.append(self.weights[name])
                except Exception as e:
                    result['predictions'][name] = {{'error': str(e)}}
            if predictions:
                counter = Counter()
                for pred, weight in zip(predictions, weights):
                    counter[pred] += weight
                result['voting_result'] = counter.most_common(1)[0][0]
                result['confidence'] = counter.most_common(1)[0][1] / sum(weights)
                consensus = len(set(predictions)) == 1
                self.stats['consensus_rate'] = (
                    self.stats['consensus_rate'] * (self.stats['calls'] - 1) + (1 if consensus else 0)
                ) / self.stats['calls']
                result['success'] = True
                self.stats['successes'] += 1
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
            self.stats['errors'] += 1
        return result

    def update_weights(self, performance: Dict[str, float]):
        for name, score in performance.items():
            if name in self.weights:
                self.weights[name] = 0.7 * self.weights[name] + 0.3 * score

def ensemble_processor(data):
    processor = EnsembleProcessor()
    return processor.process(data)
'''

    def _generate_pipeline_code(self, gen: int, libs: List[str]) -> str:
        libs_str = ', '.join(libs[:3]) if libs else 'none'
        return f'''"""
META-EVOLUTION v2.0 | Поколение: {gen}
Архитектура: Пайплайн
Источники: {libs_str}
"""
__version__ = f"meta.{gen}.0"
__meta_type__ = "pipeline"
import time
import json
import inspect
from typing import List, Dict, Any, Optional, Callable

class PipelineProcessor:
    def __init__(self):
        self.stages = []
        self.stats = {{
            'calls': 0,
            'successes': 0,
            'errors': 0,
            'stage_times': {{}},
            'start_time': time.time()
        }}
        self._build_pipeline()

    def _build_pipeline(self):
        import importlib
        libs_dir = './evolution_libs'
        stage_types = [
            ('preprocess', ['normalize', 'clean', 'transform']),
            ('analyze', ['analyze', 'calculate', 'process']),
            ('classify', ['classify', 'predict', 'detect']),
            ('postprocess', ['format', 'summarize', 'report'])
        ]
        if os.path.exists(libs_dir):
            for file in os.listdir(libs_dir):
                if file.endswith('.py') and file.startswith('evolib_'):
                    lib_name = file[:-3]
                    try:
                        spec = importlib.util.spec_from_file_location(lib_name, f'{{libs_dir}}/{{file}}')
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            for stage_name, keywords in stage_types:
                                for func_name, func in inspect.getmembers(module, inspect.isfunction):
                                    if any(kw in func_name.lower() for kw in keywords):
                                        self.stages.append({{
                                            'name': f"{{lib_name}}.{{func_name}}",
                                            'func': func,
                                            'stage': stage_name
                                        }})
                                        break
                    except Exception as e:
                        print(f"Ошибка загрузки {{lib_name}}: {{e}}")
        stage_order = {{'preprocess': 0, 'analyze': 1, 'classify': 2, 'postprocess': 3}}
        self.stages.sort(key=lambda x: stage_order.get(x['stage'], 4))

    def process(self, data: Any) -> Dict[str, Any]:
        self.stats['calls'] += 1
        result = {{
            'input_type': type(data).__name__,
            'generation': {gen},
            'stages': {{}},
            'final_result': None,
            'timestamp': time.time()
        }}
        current_data = data
        try:
            for stage in self.stages:
                start = time.time()
                try:
                    current_data = stage['func'](current_data)
                    result['stages'][stage['name']] = {{
                        'success': True,
                        'stage': stage['stage'],
                        'time': time.time() - start
                    }}
                    if stage['stage'] not in self.stats['stage_times']:
                        self.stats['stage_times'][stage['stage']] = []
                    self.stats['stage_times'][stage['stage']].append(time.time() - start)
                except Exception as e:
                    result['stages'][stage['name']] = {{
                        'success': False,
                        'error': str(e),
                        'stage': stage['stage'],
                        'time': time.time() - start
                    }}
                    break
            result['final_result'] = current_data
            result['success'] = True
            self.stats['successes'] += 1
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
            self.stats['errors'] += 1
        return result

def pipeline_processor(data):
    processor = PipelineProcessor()
    return processor.process(data)
'''

    def _generate_hierarchical_code(self, gen: int, libs: List[str]) -> str:
        libs_str = ', '.join(libs[:3]) if libs else 'none'
        return f'''"""
META-EVOLUTION v2.0 | Поколение: {gen}
Архитектура: Иерархическая
Источники: {libs_str}
"""
__version__ = f"meta.{gen}.0"
__meta_type__ = "hierarchical"
import time
import json
import inspect
from typing import List, Dict, Any, Optional
from collections import defaultdict

class HierarchicalProcessor:
    def __init__(self):
        self.layers = defaultdict(list)
        self.stats = {{
            'calls': 0,
            'successes': 0,
            'errors': 0,
            'layer_stats': {{}},
            'start_time': time.time()
        }}
        self._build_hierarchy()

    def _build_hierarchy(self):
        import importlib
        libs_dir = './evolution_libs'
        layers = {{
            'low': ['math', 'basic', 'utils'],
            'medium': ['algorithm', 'process', 'transform'],
            'high': ['ml', 'ai', 'predict', 'classify'],
            'meta': ['integrate', 'combine', 'analyze']
        }}
        if os.path.exists(libs_dir):
            for file in os.listdir(libs_dir):
                if file.endswith('.py') and file.startswith('evolib_'):
                    lib_name = file[:-3]
                    try:
                        spec = importlib.util.spec_from_file_location(lib_name, f'{{libs_dir}}/{{file}}')
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            for func_name, func in inspect.getmembers(module, inspect.isfunction):
                                if not func_name.startswith('_'):
                                    level = 'medium'
                                    for lvl, keywords in layers.items():
                                        if any(kw in func_name.lower() for kw in keywords):
                                            level = lvl
                                            break
                                    self.layers[level].append({{
                                        'name': f"{{lib_name}}.{{func_name}}",
                                        'func': func,
                                        'level': level
                                    }})
                    except Exception as e:
                        print(f"Ошибка загрузки {{lib_name}}: {{e}}")

    def process(self, data: Any) -> Dict[str, Any]:
        self.stats['calls'] += 1
        result = {{
            'input_type': type(data).__name__,
            'generation': {gen},
            'layers': {{}},
            'timestamp': time.time()
        }}
        try:
            low_result = self._process_layer('low', data)
            result['layers']['low'] = low_result
            if low_result['success']:
                medium_result = self._process_layer('medium', low_result['data'])
                result['layers']['medium'] = medium_result
                if medium_result['success']:
                    high_result = self._process_layer('high', medium_result['data'])
                    result['layers']['high'] = high_result
                    if high_result['success']:
                        meta_result = self._process_layer('meta', high_result['data'])
                        result['layers']['meta'] = meta_result
                        result['final_result'] = meta_result.get('data')
                        result['success'] = True
                        self.stats['successes'] += 1
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
            self.stats['errors'] += 1
        return result

    def _process_layer(self, layer: str, data: Any) -> Dict[str, Any]:
        result = {{
            'success': True,
            'data': data,
            'operations': []
        }}
        for func_info in self.layers.get(layer, []):
            try:
                data = func_info['func'](data)
                result['operations'].append({{
                    'name': func_info['name'],
                    'success': True
                }})
            except Exception as e:
                result['operations'].append({{
                    'name': func_info['name'],
                    'success': False,
                    'error': str(e)
                }})
                result['data'] = data
            if layer not in self.stats['layer_stats']:
                self.stats['layer_stats'][layer] = {{'calls': 0, 'successes': 0}}
            self.stats['layer_stats'][layer]['calls'] += 1
            if result['success']:
                self.stats['layer_stats'][layer]['successes'] += 1
        return result

def hierarchical_processor(data):
    processor = HierarchicalProcessor()
    return processor.process(data)
'''

    def _evaluate_meta_code(self, code: str, libs: List[LibraryRecord],
                            quality: Dict, architecture: str) -> float:
        score = 0
        is_valid, _, _, _ = self.evolution.code_analyzer.validate_syntax(code, auto_fix=False)
        if is_valid:
            score += 40
        score += quality['score'] * 0.3
        architecture_bonus = {
            'standard': 10,
            'pipeline': 20,
            'ensemble': 30,
            'hierarchical': 25,
            'adaptive': 25,
            'distributed': 30
        }
        score += architecture_bonus.get(architecture, 10)
        ml_bonus = sum(1 for lib in libs if lib.ml_models) * 15
        score += min(ml_bonus, 30)
        innovation = self._calculate_innovation_score(code, libs)
        score += innovation * 20
        if quality.get('duplicate_imports', 0) > 0:
            score -= quality['duplicate_imports'] * 5
        if quality.get('issues'):
            score -= len(quality['issues']) * 2
        return min(100, max(0, score))

    def _calculate_innovation_score(self, code: str, libs: List[LibraryRecord]) -> float:
        score = 0.5
        lib_combinations = '_'.join(sorted([lib.name for lib in libs]))
        self.innovation_tracker[lib_combinations] += 1
        if self.innovation_tracker[lib_combinations] == 1:
            score += 0.3
        if 'async' in code or 'await' in code:
            score += 0.1
        if 'ThreadPoolExecutor' in code:
            score += 0.1
        if 'Generic' in code or 'TypeVar' in code:
            score += 0.1
        lines = code.split('\n')
        if len(lines) > 100:
            score += 0.1
        return min(1.0, score)

    def get_successful_combinations(self) -> List[Tuple[str, str]]:
        """Возвращает все успешные комбинации библиотек из мета-эволюции."""
        combinations = []
        for record in self.meta_records.values():
            if record.fitness_score > 80:
                combinations.extend(record.successful_combinations)
        return list(set(combinations))

    def save_meta_history(self):
        try:
            data = {
                'meta_stats': self.meta_stats,
                'last_meta': self.last_meta_generation,
                'records': [asdict(r) for r in list(self.meta_records.values())[-20:]],
                'innovation_tracker': {str(k): v for k, v in self.innovation_tracker.items()}
            }
            with open('./meta_evolution_history.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Ошибка сохранения meta-history: {e}")

# ============================================================================
# УЛУЧШЕННЫЙ МЕНЕДЖЕР ЗДОРОВЬЯ
# ============================================================================
class HealthManager:
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.broken_libs: Set[str] = set()
        self.healed_libs: Set[str] = set()
        self.health_history: Dict[str, List[float]] = {}
        self.proactive_heal_queue: List[LibraryRecord] = []
        self.healing_stats = {
            'attempts': 0,
            'successes': 0,
            'proactive': 0,
            'deleted': 0
        }

    @measure_time
    def check_library_health(self, lib_record: LibraryRecord) -> Dict[str, Any]:
        if not os.path.exists(lib_record.path):
            return {
                'health_score': 0,
                'status': 'missing',
                'action': 'delete',
                'reason': 'Файл не найден'
            }
        try:
            with open(lib_record.path, 'r', encoding='utf-8') as f:
                code = f.read()
        except Exception as e:
            return {
                'health_score': 0,
                'status': 'unreadable',
                'action': 'delete',
                'reason': f'Не читается: {e}'
            }
        health_check = self.evolution.code_analyzer.validate_library_health(code)
        health_score = 100
        if not health_check['is_valid']:
            health_score -= 50
            health_score -= len(health_check['syntax_errors']) * 10
            health_score -= len(health_check['import_issues']) * 15
            health_score -= health_check['duplicate_imports'] * 5
            health_score -= len(health_check['broken_functions']) * 20
        if health_check['quality_score'] < health_score:
            health_score = health_check['quality_score']
        health_score = max(0, min(100, health_score))
        action = 'keep'
        reason = f'Здорова ({health_score:.0f})'
        if health_score < 30:
            action = 'delete'
            reason = f'Критическое состояние ({health_score:.0f})'
        elif health_score < 60:
            if lib_record.healing_attempts < CONFIG['HEALING_ATTEMPTS']:
                action = 'fix'
                reason = f'Требуется исцеление ({health_score:.0f})'
            else:
                action = 'delete'
                reason = f'Слишком много попыток ({lib_record.healing_attempts})'
        elif health_score < 75 and CONFIG['ENABLE_PROACTIVE_HEALING']:
            if lib_record.times_used > 0 and lib_record.fitness_score > 70:
                action = 'proactive'
                reason = f'Проактивное исцеление ({health_score:.0f})'
        if lib_record.name not in self.health_history:
            self.health_history[lib_record.name] = []
        self.health_history[lib_record.name].append(health_score)
        return {
            'health_score': health_score,
            'status': health_check['recommend_action'],
            'action': action,
            'reason': reason,
            'syntax_errors': health_check['syntax_errors'],
            'import_issues': health_check['import_issues'],
            'quality_score': health_check['quality_score'],
            'function_count': health_check['function_count'],
            'duplicate_imports': health_check['duplicate_imports'],
            'broken_functions': health_check['broken_functions']
        }

    def cleanup_broken_libraries(self) -> Tuple[int, int]:
        removed = 0
        healed = 0
        healing_attempts = 0
        proactive = 0
        libs_to_check = list(self.evolution.library_creator.libraries.values())
        random.shuffle(libs_to_check)
        for lib in libs_to_check[:CONFIG['MAX_HEALED_PER_CYCLE'] * 3]:
            health = self.check_library_health(lib)
            if health['action'] == 'delete':
                if self._delete_library(lib, health['reason']):
                    removed += 1
                    self.broken_libs.add(lib.name)
                    self.healing_stats['deleted'] += 1
            elif health['action'] == 'fix':
                lib.healing_attempts += 1
                lib.last_healing_attempt = datetime.now().isoformat()
                healing_attempts += 1
                if self._heal_library(lib, health):
                    healed += 1
                    lib.times_healed += 1
                    self.healed_libs.add(lib.name)
                    self.healing_stats['successes'] += 1
                if health['duplicate_imports'] > 0:
                    self.evolution.state.removed_duplicate_imports += health['duplicate_imports']
                if health['broken_functions']:
                    self.evolution.state.fixed_broken_functions += len(health['broken_functions'])
            elif health['action'] == 'proactive':
                if lib.name not in [l.name for l in self.proactive_heal_queue]:
                    self.proactive_heal_queue.append(lib)
                    proactive += 1
                    self.healing_stats['proactive'] += 1
        self.evolution.state.healing_attempts += healing_attempts
        self.healing_stats['attempts'] += healing_attempts
        return removed, healed

    def process_proactive_queue(self) -> int:
        healed = 0
        queue = self.proactive_heal_queue[:CONFIG['MAX_HEALED_PER_CYCLE']]
        self.proactive_heal_queue = self.proactive_heal_queue[CONFIG['MAX_HEALED_PER_CYCLE']:]
        for lib in queue:
            lib.healing_attempts += 1
            lib.last_healing_attempt = datetime.now().isoformat()
            health = self.check_library_health(lib)
            if self._heal_library(lib, health):
                healed += 1
                lib.times_healed += 1
                self.healed_libs.add(lib.name)
                self.evolution.state.proactive_heals += 1
                self.healing_stats['proactive'] += 1
        return healed

    def _heal_library(self, lib: LibraryRecord, health: Dict[str, Any]) -> bool:
        try:
            with open(lib.path, 'r', encoding='utf-8') as f:
                code = f.read()
            fixed_code, fixed_count, fixes_applied = self.evolution.code_analyzer.syntax_fixer.fix_all(code)
            if fixed_count > 0:
                is_valid, _, _, _ = self.evolution.code_analyzer.validate_syntax(fixed_code, auto_fix=False)
                if is_valid:
                    backup_path = lib.path + '.bak'
                    if os.path.exists(backup_path):
                        os.remove(backup_path)
                    os.rename(lib.path, backup_path)
                    with open(lib.path, 'w', encoding='utf-8') as f:
                        f.write(fixed_code)
                    action = "🩺" if lib.healing_attempts <= 3 else "🔧"
                    logger.info(f"{action} Исцелена {lib.name} (попытка {lib.healing_attempts}, исправлено {fixed_count})")
                    self.evolution.state.healed_libraries += 1
                    self.evolution.state.successful_healing += 1
                    if 'импорты' in str(fixes_applied):
                        self.evolution.state.added_imports += 1
                    if 'дублирующиеся' in str(fixes_applied):
                        self.evolution.state.removed_duplicate_imports += health.get('duplicate_imports', 1)
                    if 'сломанные' in str(fixes_applied):
                        self.evolution.state.fixed_broken_functions += 1
                    if 'мёртвый' in str(fixes_applied):
                        self.evolution.state.removed_dead_code += 1
                    return True
            return False
        except Exception as e:
            logger.error(f"Ошибка при исцелении {lib.name}: {e}")
            return False

    def _delete_library(self, lib: LibraryRecord, reason: str) -> bool:
        try:
            if os.path.exists(lib.path):
                os.remove(lib.path)
                lib.is_active = False
                lib.health_score = 0
                patterns_to_remove = []
                for pid, pattern in self.evolution.code_pool.patterns.items():
                    if pattern.id == lib.name or lib.name in pattern.uses_libraries:
                        patterns_to_remove.append(pid)
                for pid in patterns_to_remove:
                    if pid in self.evolution.code_pool.patterns:
                        if pid in self.evolution.code_pool.elite_patterns:
                            self.evolution.code_pool.elite_patterns.remove(pid)
                        del self.evolution.code_pool.patterns[pid]
                logger.info(f"🗑️ Удалена библиотека: {lib.name} (причина: {reason})")
                return True
        except Exception as e:
            logger.error(f"Ошибка при удалении {lib.name}: {e}")
        return False

    def cleanup_unused_libraries(self) -> int:
        removed = 0
        current_gen = self.evolution.state.generation
        libs_to_check = list(self.evolution.library_creator.libraries.values())
        for lib in libs_to_check:
            if not lib.is_active:
                continue
            age_in_generations = current_gen - lib.generation
            delete_reason = None
            if lib.fitness_score < CONFIG['LOW_FITNESS_THRESHOLD'] and lib.times_used < 1:
                if lib.healing_attempts >= CONFIG['HEALING_ATTEMPTS'] or age_in_generations > CONFIG['CLEANUP_OLD_GENERATIONS']:
                    delete_reason = f"низкий fitness ({lib.fitness_score:.0f})"
            elif age_in_generations > CONFIG['CLEANUP_OLD_GENERATIONS'] * 2 and lib.times_used < 1 and lib.times_used_as_source < 1:
                delete_reason = f"старая и неиспользуемая (возраст {age_in_generations})"
            elif lib.duplicate_imports > CONFIG['MAX_DUPLICATE_IMPORTS'] * 3:
                delete_reason = f"много дублирующихся импортов ({lib.duplicate_imports})"
            elif len(lib.broken_functions) > 5:
                delete_reason = f"много сломанных функций ({len(lib.broken_functions)})"
            if delete_reason:
                if self._delete_library(lib, delete_reason):
                    removed += 1
                    self.evolution.state.removed_unused_libraries += 1
        return removed

    def get_unhealthy_libraries(self, threshold: float = 60.0) -> List[LibraryRecord]:
        unhealthy = []
        for lib in self.evolution.library_creator.libraries.values():
            if lib.is_active:
                health = self.check_library_health(lib)
                if health['health_score'] < threshold:
                    unhealthy.append(lib)
        return unhealthy

    def get_healthiest_libraries(self, count: int = 10) -> List[LibraryRecord]:
        libs_with_health = []
        for lib in self.evolution.library_creator.libraries.values():
            if lib.is_active:
                health = self.check_library_health(lib)
                libs_with_health.append((lib, health['health_score']))
        libs_with_health.sort(key=lambda x: x[1], reverse=True)
        return [lib for lib, _ in libs_with_health[:count]]

    def get_stats(self) -> Dict[str, Any]:
        return {
            'healing_stats': self.healing_stats,
            'broken_libs': len(self.broken_libs),
            'healed_libs': len(self.healed_libs),
            'queue_size': len(self.proactive_heal_queue),
            'avg_health': self.evolution.state.avg_health_score
        }

# ============================================================================
# УЛУЧШЕННЫЙ СОЗДАТЕЛЬ БИБЛИОТЕК (С ВАЛИДАЦИЕЙ)
# ============================================================================
class LibraryCreator:
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.libraries: Dict[str, LibraryRecord] = {}
        self.code_analyzer = CodeAnalyzer()
        self.last_cleanup = time.time()
        self.creation_stats = defaultdict(int)
        self.library_cache = {}
        self.syntax_validator = SyntaxValidator()
        Path(CONFIG['LIBRARIES_DIR']).mkdir(exist_ok=True)
        if CONFIG['LIBRARIES_DIR'] not in sys.path:
            sys.path.insert(0, CONFIG['LIBRARIES_DIR'])
        self.load_existing()

    def _check_and_create_dependencies(self, code: str):
        """Проверяет и создаёт недостающие зависимости в коде."""
        import re
        # Ищем все импорты вида 'from evolution_libs.xxx import yyy'
        pattern = r"from evolution_libs\.(\w+) import"
        matches = re.findall(pattern, code)
        
        for dep in matches:
            if dep not in self.libraries and self.evolution and self.evolution.dependency_creator:
                logger.info(f"🔍 Обнаружена зависимость от {dep}, создаём...")
                self.evolution.dependency_creator.ensure_dependency(dep)

    @measure_time
    def load_existing(self):
        """Загружает существующие библиотеки с обработкой ошибок импорта."""
        for lib_file in Path(CONFIG['LIBRARIES_DIR']).glob('evolib_*.py'):
            try:
                lib_name = lib_file.stem
                content = lib_file.read_text(encoding='utf-8')
                
                # Сначала проверяем и создаём недостающие зависимости
                self._check_and_create_dependencies(content)
                
                # Проверяем синтаксис через валидатор
                is_valid, fixed_content, errors = self.syntax_validator.validate_and_fix(
                    content, auto_fix=CONFIG['FIX_SYNTAX_AUTO']
                )
                
                if not is_valid:
                    logger.error(f"❌ Пропуск битой библиотеки {lib_name}: {errors}")
                    continue
                    
                if fixed_content != content:
                    lib_file.write_text(fixed_content, encoding='utf-8')
                    logger.info(f"🔧 Исправлен синтаксис {lib_name}")
                    if self.evolution:
                        self.evolution.state.fixed_syntax_errors += 1
                    content = fixed_content
                
                health_check = self.code_analyzer.validate_library_health(content)
                
                # Пробуем загрузить модуль
                try:
                    spec = importlib.util.spec_from_file_location(lib_name, str(lib_file))
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        
                        exported = [name for name, obj in inspect.getmembers(module)
                                    if inspect.isfunction(obj) and not name.startswith('_')]
                        classes = [name for name, obj in inspect.getmembers(module)
                                   if inspect.isclass(obj) and not name.startswith('_')]
                        ml_models = [name for name, obj in inspect.getmembers(module)
                                     if inspect.isclass(obj) and any(
                                x in name.lower() for x in ['neural', 'network', 'model', 'classifier']
                            )]
                        quality = self.code_analyzer.check_code_quality(content)
                        
                        if self.evolution:
                            self.libraries[lib_name] = LibraryRecord(
                                name=lib_name, 
                                path=str(lib_file), 
                                purpose='Загружена',
                                generation=self.evolution.state.generation,
                                times_used=0, 
                                tests_passed=0, 
                                tests_total=0,
                                created_at=datetime.fromtimestamp(lib_file.stat().st_ctime).isoformat(),
                                fitness_score=quality['score'],
                                exported_functions=exported,
                                exported_classes=classes,
                                ml_models=ml_models,
                                is_active=True,
                                error_count=0,
                                validation_status=is_valid,
                                health_score=health_check['quality_score'],
                                last_used_generation=0,
                                times_used_as_source=0,
                                duplicate_imports=health_check.get('duplicate_imports', 0),
                                broken_functions=health_check.get('broken_functions', []),
                                healing_attempts=0,
                                times_healed=0,
                                times_optimized=0,
                                size_bytes=lib_file.stat().st_size,
                                lines_of_code=quality['code_lines'],
                                complexity_score=quality['complexity']
                            )
                            logger.info(f"✅ Загружена библиотека: {lib_name}")
                        
                except ImportError as e:
                    logger.warning(f"⚠️ Ошибка импорта {lib_name}: {e}")
                    # Пытаемся создать недостающие зависимости и загрузить снова
                    if self.evolution and self.evolution.dependency_creator:
                        # Извлекаем имена отсутствующих модулей из ошибки
                        import re
                        match = re.search(r"No module named '([^']+)'", str(e))
                        if match:
                            missing_module = match.group(1)
                            if self.evolution.dependency_creator.ensure_dependency(missing_module):
                                logger.info(f"✅ Создана зависимость {missing_module}, пробуем снова")
                                # Повторная попытка загрузки
                                try:
                                    spec = importlib.util.spec_from_file_location(lib_name, str(lib_file))
                                    if spec and spec.loader:
                                        module = importlib.util.module_from_spec(spec)
                                        spec.loader.exec_module(module)
                                        logger.info(f"✅ Успешная загрузка {lib_name} после создания зависимостей")
                                except Exception as e2:
                                    logger.error(f"❌ Повторная ошибка загрузки {lib_name}: {e2}")
                            
            except Exception as e:
                logger.error(f"Ошибка загрузки {lib_file.name}: {e}")

    @measure_time
    def create_library(self, goal: str, use_evolution: bool = True) -> Optional[str]:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        lib_name = f"evolib_{goal}_{timestamp}"
        lib_file = Path(CONFIG['LIBRARIES_DIR']) / f"{lib_name}.py"
        if use_evolution and self.evolution.code_pool.patterns:
            content = self._generate_evolved_content(goal)
        else:
            content = self._generate_advanced_content(goal)
        if random.random() < CONFIG['LIBRARY_USAGE_PROBABILITY']:
            content = self._add_library_usage(content, goal)
        
        # Проверяем синтаксис через валидатор
        is_valid, fixed_content, errors = self.syntax_validator.validate_and_fix(
            content, auto_fix=True
        )
        
        if not is_valid:
            self.evolution.state.rejected_syntax_errors += 1
            logger.error(f"❌ Синтаксическая ошибка в {lib_name}: {errors}")
            logger.info("🔄 Используем базовый шаблон")
            content = self._generate_advanced_content(goal)
            is_valid, fixed_content, errors = self.syntax_validator.validate_and_fix(
                content, auto_fix=False
            )
            if not is_valid:
                logger.error(f"❌ Критическая ошибка в шаблоне: {errors}")
                return None
        elif fixed_content != content:
            logger.info(f"🔧 Исправлен синтаксис {lib_name}")
            self.evolution.state.auto_fixed_syntax += 1
            content = fixed_content
        
        with open(lib_file, 'w', encoding='utf-8') as f:
            f.write(content)
        module = self._load_module(lib_name, str(lib_file))
        tests_passed, tests_total = self._test_library(module, goal)
        metadata = self.code_analyzer.extract_metadata(content)
        quality = self.code_analyzer.check_code_quality(content)
        fitness = quality['score'] * 0.4 + (tests_passed / max(1, tests_total)) * 40 + (
                len(metadata['functions']) * 2
        )
        lib_record = LibraryRecord(
            name=lib_name, path=str(lib_file),
            purpose=EVOLUTION_GOALS[goal]['name'],
            generation=self.evolution.state.generation + 1,
            times_used=0, tests_passed=tests_passed, tests_total=tests_total,
            created_at=datetime.now().isoformat(),
            fitness_score=fitness,
            exported_functions=[f['name'] for f in metadata['functions']],
            exported_classes=[c['name'] for c in metadata['classes']],
            ml_models=self._extract_ml_models(module),
            is_active=True,
            error_count=0,
            validation_status=True,
            health_score=quality['score'],
            last_used_generation=self.evolution.state.generation + 1,
            times_used_as_source=0,
            duplicate_imports=quality.get('duplicate_imports', 0),
            broken_functions=[],
            healing_attempts=0,
            times_healed=0,
            times_optimized=0,
            size_bytes=lib_file.stat().st_size,
            lines_of_code=quality['code_lines'],
            complexity_score=quality['complexity']
        )
        self.libraries[lib_name] = lib_record
        self.creation_stats[goal] += 1
        if tests_passed > 0 and quality['score'] >= CONFIG['QUALITY_THRESHOLD']:
            pattern = CodePattern(
                id=lib_name, code=content, category=goal,
                fitness_score=fitness, usage_count=0,
                success_rate=tests_passed / max(1, tests_total),
                parent_ids=[], generation=self.evolution.state.generation,
                created_at=datetime.now().isoformat(),
                complexity=quality['complexity'],
                is_elite=fitness > 85 and quality['score'] > 85,
                uses_libraries=self._extract_used_libraries(content),
                error_count=0,
                validation_status=True,
                quality_score=quality['score'],
                function_count=len(metadata['functions']),
                class_count=len(metadata['classes']),
                has_duplicates=quality.get('duplicate_imports', 0) > 0,
                syntax_valid=True
            )
            self.evolution.code_pool.add_pattern(pattern, self.evolution)
        status = "✅" if tests_passed == tests_total and tests_total > 0 else "⚠️"
        logger.info(f"📚 {status} Библиотека: {lib_name} (fitness: {fitness:.0f}, качество: {quality['score']:.0f}, тесты: {tests_passed}/{tests_total})")
        if lib_record.ml_models:
            self.evolution.state.ml_models_created += len(lib_record.ml_models)
        return lib_name

    def _generate_advanced_content(self, goal: str) -> str:
        gen = self.evolution.state.generation + 1
        templates = {
            'ml_ai': self._get_ml_template(gen),
            'math': self._get_math_template(gen),
            'algorithms': self._get_algorithms_template(gen),
            'integration': self._get_integration_template(gen),
            'network': self._get_network_template(gen),
            'database': self._get_database_template(gen),
            'security': self._get_security_template(gen),
            'visualization': self._get_visualization_template(gen),
            'strings': self._get_strings_template(gen),
            'files': self._get_files_template(gen)
        }
        return templates.get(goal, self._get_default_template(gen))

    def _get_ml_template(self, gen: int) -> str:
        return f'''"""
🤖 ML/AI библиотека | Поколение: {gen}
Тип: Продвинутая ML библиотека
"""
from typing import List, Dict, Any, Tuple, Optional, Union
import random
import math
import statistics
from collections import defaultdict

__version__ = f"ml.{gen}.0"
__ml_type__ = "advanced"

class NeuralNetwork:
    def __init__(self, input_size: int = 10, hidden_sizes: List[int] = None, output_size: int = 2):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes or [5, 3]
        self.output_size = output_size
        self.weights = []
        self.biases = []
        prev_size = input_size
        for hidden_size in self.hidden_sizes:
            self.weights.append([[random.uniform(-0.1, 0.1) for _ in range(hidden_size)]
                                 for _ in range(prev_size)])
            self.biases.append([random.uniform(-0.1, 0.1) for _ in range(hidden_size)])
            prev_size = hidden_size
        self.weights.append([[random.uniform(-0.1, 0.1) for _ in range(output_size)]
                             for _ in range(prev_size)])
        self.biases.append([random.uniform(-0.1, 0.1) for _ in range(output_size)])
        self.trained = False
        self.training_history = []

    def sigmoid(self, x: float) -> float:
        try:
            if x < -500:
                return 0
            if x > 500:
                return 1
            return 1 / (1 + math.exp(-x))
        except Exception:
            return 0.5

    def sigmoid_derivative(self, x: float) -> float:
        s = self.sigmoid(x)
        return s * (1 - s)

    def forward(self, inputs: List[float]) -> List[float]:
        if len(inputs) != self.input_size:
            return [0.5] * self.output_size
        current = inputs
        for layer_weights, layer_biases in zip(self.weights, self.biases):
            next_layer = []
            for j in range(len(layer_biases)):
                z = sum(current[i] * layer_weights[i][j] for i in range(len(current)))
                z += layer_biases[j]
                next_layer.append(self.sigmoid(z))
            current = next_layer
        return current

    def predict(self, inputs: List[float]) -> Union[List[float], Dict[str, Any]]:
        if isinstance(inputs[0], list):
            return [self.predict(x) for x in inputs]
        outputs = self.forward(inputs)
        return {{
            'outputs': outputs,
            'class': max(range(len(outputs)), key=lambda i: outputs[i]),
            'confidence': max(outputs),
            'probabilities': outputs
        }}

    def train(self, training_data: List[Tuple[List[float], List[float]]],
              epochs: int = 100, learning_rate: float = 0.1) -> Dict[str, Any]:
        try:
            for epoch in range(epochs):
                total_loss = 0
                for inputs, targets in training_data:
                    activations = [inputs]
                    zs = []
                    current = inputs
                    for layer_weights, layer_biases in zip(self.weights, self.biases):
                        z = [sum(current[i] * layer_weights[i][j] for i in range(len(current)))
                             + layer_biases[j] for j in range(len(layer_biases))]
                        zs.append(z)
                        current = [self.sigmoid(z_val) for z_val in z]
                        activations.append(current)
                    delta = [(activations[-1][i] - targets[i]) *
                             self.sigmoid_derivative(zs[-1][i])
                             for i in range(len(targets))]
                    for l in range(len(self.weights) - 1, -1, -1):
                        for i in range(len(self.weights[l])):
                            for j in range(len(self.weights[l][i])):
                                self.weights[l][i][j] -= learning_rate * delta[j] * activations[l][i]
                        for j in range(len(self.biases[l])):
                            self.biases[l][j] -= learning_rate * delta[j]
                        if l > 0:
                            new_delta = [0] * len(self.weights[l - 1][0])
                            for i in range(len(self.weights[l - 1][0])):
                                error = sum(delta[j] * self.weights[l][i][j] for j in range(len(delta)))
                                new_delta[i] = error * self.sigmoid_derivative(zs[l - 1][i])
                            delta = new_delta
                    loss = sum((activations[-1][i] - targets[i]) ** 2 for i in range(len(targets)))
                    total_loss += loss
                self.training_history.append(total_loss / len(training_data))
            self.trained = True
        except Exception as e:
            return {{'error': str(e)}}
        return {{
            'epochs': epochs,
            'trained': self.trained,
            'final_loss': self.training_history[-1] if self.training_history else 0,
            'loss_history': self.training_history[-10:]
        }}

    def save_model(self, path: str) -> bool:
        try:
            import json
            model_data = {{
                'input_size': self.input_size,
                'hidden_sizes': self.hidden_sizes,
                'output_size': self.output_size,
                'weights': self.weights,
                'biases': self.biases,
                'trained': self.trained,
                'training_history': self.training_history
            }}
            with open(path, 'w') as f:
                json.dump(model_data, f)
            return True
        except Exception:
            return False

    def load_model(self, path: str) -> bool:
        try:
            import json
            with open(path, 'r') as f:
                model_data = json.load(f)
            self.input_size = model_data['input_size']
            self.hidden_sizes = model_data['hidden_sizes']
            self.output_size = model_data['output_size']
            self.weights = model_data['weights']
            self.biases = model_data['biases']
            self.trained = model_data['trained']
            self.training_history = model_data.get('training_history', [])
            return True
        except Exception:
            return False

class AdvancedClassifier:
    def __init__(self, n_classes: int = 2):
        self.n_classes = n_classes
        self.models = []
        self.weights = []

    def add_model(self, model: Any, weight: float = 1.0):
        self.models.append(model)
        self.weights.append(weight)

    def predict(self, data: List[float]) -> Dict[str, Any]:
        if not self.models:
            return {{'class': -1, 'confidence': 0}}
        predictions = []
        confidences = []
        for model, weight in zip(self.models, self.weights):
            try:
                if hasattr(model, 'predict'):
                    pred = model.predict(data)
                    if isinstance(pred, dict):
                        predictions.append(pred.get('class', 0))
                        confidences.append(pred.get('confidence', 0) * weight)
                    else:
                        predictions.append(pred)
                        confidences.append(weight)
            except Exception:
                pass
        if not predictions:
            return {{'class': -1, 'confidence': 0}}
        from collections import Counter
        vote_count = Counter()
        for pred, conf in zip(predictions, confidences):
            vote_count[pred] += conf
        best_class, best_vote = vote_count.most_common(1)[0]
        return {{
            'class': best_class,
            'confidence': best_vote / sum(confidences),
            'votes': dict(vote_count),
            'n_models': len(self.models)
        }}

def create_ml_pipeline(input_size: int = 10) -> Dict[str, Any]:
    return {{
        'preprocess': lambda x: [(v - min(x)) / (max(x) - min(x) + 1e-8) for v in x],
        'model': NeuralNetwork(input_size, [5], 2),
        'postprocess': lambda x: x
    }}

def analyze_data(data: List[float]) -> Dict[str, Any]:
    if not data:
        return {{'error': 'Нет данных'}}
    stats = {{
        'count': len(data),
        'mean': sum(data) / len(data),
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data)
    }}
    if len(data) > 1:
        stats['variance'] = sum((x - stats['mean']) ** 2 for x in data) / len(data)
        stats['std'] = math.sqrt(stats['variance'])
    return stats
'''

    def _get_math_template(self, gen: int) -> str:
        return f'''"""
🧮 Математическая библиотека | Поколение: {gen}
"""
from typing import List, Dict, Any, Optional, Union
import statistics
import math
from functools import reduce

__version__ = f"math.{gen}.0"

def calculate_stats(data: List[float]) -> Dict[str, Any]:
    if not data:
        return {{}}
    n = len(data)
    mean = sum(data) / n
    sorted_data = sorted(data)
    result = {{
        'count': n,
        'sum': sum(data),
        'mean': mean,
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data),
        'median': statistics.median(data) if n > 0 else 0
    }}
    if n > 1:
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
        result.update({{
            'variance': variance,
            'std': math.sqrt(variance),
            'q1': sorted_data[n // 4] if n >= 4 else sorted_data[0],
            'q3': sorted_data[3 * n // 4] if n >= 4 else sorted_data[-1],
            'iqr': (sorted_data[3 * n // 4] - sorted_data[n // 4]) if n >= 4 else 0
        }})
    return result

def find_median(data: List[float]) -> float:
    if not data:
        return 0
    n = len(data)
    if n <= 2:
        return sum(data) / n
    try:
        return statistics.median(data)
    except Exception:
        s = sorted(data)
        mid = n // 2
        return s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2

def normalize_data(data: List[float], method: str = 'minmax') -> List[float]:
    if not data:
        return []
    if method == 'minmax':
        min_val = min(data)
        max_val = max(data)
        if max_val == min_val:
            return [0.5] * len(data)
        return [(x - min_val) / (max_val - min_val) for x in data]
    elif method == 'zscore':
        mean = sum(data) / len(data)
        std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
        if std == 0:
            return [0] * len(data)
        return [(x - mean) / std for x in data]
    elif method == 'robust':
        median = find_median(data)
        q1 = statistics.quantiles(data, n=4)[0] if len(data) >= 4 else median
        q3 = statistics.quantiles(data, n=4)[2] if len(data) >= 4 else median
        iqr = q3 - q1
        if iqr == 0:
            return [0] * len(data)
        return [(x - median) / iqr for x in data]
    return data

def correlation(x: List[float], y: List[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        return 0
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / (n - 1))
    std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / (n - 1))
    if std_x == 0 or std_y == 0:
        return 0
    return cov / ((n - 1) * std_x * std_y)

def moving_average(data: List[float], window: int = 3) -> List[float]:
    if len(data) < window:
        return data
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i + window]) / window)
    return result

def detect_outliers(data: List[float], method: str = 'iqr') -> List[int]:
    if len(data) < 4:
        return []
    if method == 'iqr':
        q1 = statistics.quantiles(data, n=4)[0]
        q3 = statistics.quantiles(data, n=4)[2]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return [i for i, x in enumerate(data) if x < lower_bound or x > upper_bound]
    elif method == 'zscore':
        mean = sum(data) / len(data)
        std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
        if std == 0:
            return []
        return [i for i, x in enumerate(data) if abs(x - mean) > 3 * std]
    return []
'''

    def _get_algorithms_template(self, gen: int) -> str:
        return f'''"""
🔍 Алгоритмическая библиотека | Поколение: {gen}
"""
from typing import List, Dict, Any, Optional, TypeVar, Generic
import heapq
from collections import deque

T = TypeVar('T')
__version__ = f"algo.{gen}.0"

class PriorityQueue(Generic[T]):
    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item: T, priority: float = 0):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self) -> T:
        return heapq.heappop(self._heap)[2]

    def peek(self) -> Optional[T]:
        return self._heap[0][2] if self._heap else None

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

class Graph:
    def __init__(self):
        self.adjacency = {{}}

    def add_edge(self, u: Any, v: Any, weight: float = 1):
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        self.adjacency[u].append((v, weight))

    def bfs(self, start: Any) -> List[Any]:
        if start not in self.adjacency:
            return []
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            result.append(node)
            for neighbor, _ in self.adjacency.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
        return result

    def dfs(self, start: Any) -> List[Any]:
        if start not in self.adjacency:
            return []
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            result.append(node)
            for neighbor, _ in self.adjacency.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        return result

    def shortest_path(self, start: Any, end: Any) -> Optional[List[Any]]:
        if start not in self.adjacency or end not in self.adjacency:
            return None
        distances = {{node: float('inf') for node in self.adjacency}}
        distances[start] = 0
        previous = {{node: None for node in self.adjacency}}
        pq = [(0, start)]
        while pq:
            current_dist, current = heapq.heappop(pq)
            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = previous[current]
                return list(reversed(path))
            if current_dist > distances[current]:
                continue
            for neighbor, weight in self.adjacency.get(current, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        return None

def binary_search(arr: List[T], target: T) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def quick_sort(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[T], right: List[T]) -> List[T]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def find_duplicates(arr: List[T]) -> List[T]:
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def longest_common_subsequence(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]
'''

    def _get_integration_template(self, gen: int) -> str:
        return f'''"""
🔗 Интеграционная библиотека | Поколение: {gen}
Тип: Системная интеграция
"""
from typing import Any, Dict, List, Optional, Callable
import json
import inspect
from functools import wraps

__version__ = f"integ.{gen}.0"

class Pipeline:
    def __init__(self):
        self.stages = []
        self.context = {{}}

    def add_stage(self, func: Callable, name: Optional[str] = None):
        self.stages.append({{
            'func': func,
            'name': name or func.__name__
        }})
        return self

    def add_condition(self, condition: Callable, true_stage: Callable, false_stage: Optional[Callable] = None):
        def conditional(data):
            if condition(data):
                return true_stage(data)
            elif false_stage:
                return false_stage(data)
            return data
        stage_name = "if_" + true_stage.__name__
        self.stages.append({{
            'func': conditional,
            'name': stage_name
        }})
        return self

    def execute(self, data: Any) -> Dict[str, Any]:
        result = {{
            'success': True,
            'data': data,
            'stages': [],
            'errors': []
        }}
        current = data
        for stage in self.stages:
            try:
                current = stage['func'](current)
                result['stages'].append({{
                    'name': stage['name'],
                    'success': True
                }})
            except Exception as e:
                result['stages'].append({{
                    'name': stage['name'],
                    'success': False,
                    'error': str(e)
                }})
                result['errors'].append(str(e))
                result['success'] = False
                break
        result['data'] = current
        return result

    def parallel(self, *funcs: Callable) -> Callable:
        def wrapper(data):
            results = []
            for func in funcs:
                try:
                    results.append(func(data))
                except Exception as e:
                    results.append({{'error': str(e)}})
            return results
        return wrapper

    def compose(self, *funcs: Callable) -> Callable:
        def composed(data):
            result = data
            for func in funcs:
                result = func(result)
            return result
        return composed

class Adapter:
    @staticmethod
    def adapt_input(func: Callable, input_mapping: Dict[str, str]):
        @wraps(func)
        def wrapper(**kwargs):
            adapted_kwargs = {{}}
            for old_name, new_name in input_mapping.items():
                if new_name in kwargs:
                    adapted_kwargs[old_name] = kwargs[new_name]
            return func(**adapted_kwargs)
        return wrapper

    @staticmethod
    def adapt_output(func: Callable, output_mapping: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return output_mapping(result)
        return wrapper

    @staticmethod
    def chain(*funcs: Callable) -> Callable:
        def chained(data):
            for func in funcs:
                data = func(data)
            return data
        return chained

class ServiceRegistry:
    def __init__(self):
        self._services = {{}}
        self._instances = {{}}

    def register(self, name: str, service: Any, singleton: bool = True):
        self._services[name] = {{
            'class': service if isinstance(service, type) else type(service),
            'singleton': singleton,
            'instance': service if not isinstance(service, type) and singleton else None
        }}

    def get(self, name: str) -> Optional[Any]:
        if name not in self._services:
            return None
        service_info = self._services[name]
        if service_info['singleton']:
            if service_info['instance'] is None:
                service_info['instance'] = service_info['class']()
            return service_info['instance']
        return service_info['class']()

    def list_services(self) -> List[str]:
        return list(self._services.keys())

class EventBus:
    def __init__(self):
        self._handlers = {{}}

    def subscribe(self, event: str, handler: Callable):
        if event not in self._handlers:
            self._handlers[event] = []
        self._handlers[event].append(handler)

    def publish(self, event: str, data: Any = None):
        if event in self._handlers:
            for handler in self._handlers[event]:
                try:
                    handler(data)
                except Exception:
                    pass

    def unsubscribe(self, event: str, handler: Callable):
        if event in self._handlers and handler in self._handlers[event]:
            self._handlers[event].remove(handler)

def integrate_systems(system1: Callable, system2: Callable, strategy: str = 'chain') -> Callable:
    if strategy == 'chain':
        def integrated(data):
            result1 = system1(data)
            return system2(result1)
    elif strategy == 'parallel':
        def integrated(data):
            return {{
                'system1': system1(data),
                'system2': system2(data)
            }}
    elif strategy == 'conditional':
        def integrated(data):
            result1 = system1(data)
            if result1 and result1.get('success', False):
                return system2(data)
            return result1
    else:
        def integrated(data):
            return system2(system1(data))
    return integrated
'''

    def _get_default_template(self, gen: int) -> str:
        return f'''"""
Базовая библиотека | Поколение: {gen}
"""
from typing import Any, Dict, List, Optional

__version__ = f"base.{gen}.0"

def process(data: Any) -> Dict[str, Any]:
    """Базовая обработка данных"""
    return {{
        'success': True,
        'data': data,
        'type': type(data).__name__
    }}
'''

    def _get_network_template(self, gen: int) -> str:
        return f'''"""
🌐 Сетевая библиотека | Поколение: {gen}
"""
import socket
import requests
from typing import Dict, Any, Optional

def fetch_url(url: str) -> Dict[str, Any]:
    try:
        response = requests.get(url, timeout=5)
        return {{
            'success': True,
            'status': response.status_code,
            'data': response.text[:1000],
            'headers': dict(response.headers)
        }}
    except Exception as e:
        return {{'success': False, 'error': str(e)}}
'''

    def _get_database_template(self, gen: int) -> str:
        return f'''"""
💾 База данных | Поколение: {gen}
"""
import sqlite3
from typing import Dict, Any, List

def query_db(db_path: str, query: str) -> Dict[str, Any]:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return {{'success': True, 'data': data, 'count': len(data)}}
    except Exception as e:
        return {{'success': False, 'error': str(e)}}
'''

    def _get_security_template(self, gen: int) -> str:
        return f'''"""
🔐 Безопасность | Поколение: {gen}
"""
import hashlib
import base64

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def encode_base64(data: str) -> str:
    return base64.b64encode(data.encode()).decode()
'''

    def _get_visualization_template(self, gen: int) -> str:
        return f'''"""
📊 Визуализация | Поколение: {gen}
"""
from typing import List, Dict, Any

def create_chart(data: List[float]) -> Dict[str, Any]:
    return {{
        'type': 'line',
        'data': data,
        'labels': [str(i) for i in range(len(data))],
        'min': min(data) if data else 0,
        'max': max(data) if data else 0
    }}
'''

    def _get_strings_template(self, gen: int) -> str:
        return f'''"""
📝 Текст | Поколение: {gen}
"""
from typing import List, Dict, Any

def process_text(text: str) -> Dict[str, Any]:
    return {{
        'length': len(text),
        'words': len(text.split()),
        'lines': len(text.split('\\n')),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }}
'''

    def _get_files_template(self, gen: int) -> str:
        return f'''"""
📁 Файлы | Поколение: {gen}
"""
import os
from typing import Dict, Any

def read_file(path: str) -> Dict[str, Any]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {{
            'success': True,
            'content': content,
            'size': os.path.getsize(path)
        }}
    except Exception as e:
        return {{'success': False, 'error': str(e)}}
'''

    def _generate_evolved_content(self, goal: str) -> str:
        best = self.evolution.code_pool.get_best_patterns(
            goal, 3, min_quality=CONFIG['MIN_QUALITY_FOR_PARENT']
        )
        if len(best) >= 2 and random.random() < CONFIG['CROSSOVER_RATE']:
            child_code, parents = self.evolution.code_pool.crossover(best[0], best[1])
            child_code = self.evolution.code_pool.mutate(child_code, CONFIG['MUTATION_RATE'])
            return child_code
        elif best:
            return self.evolution.code_pool.mutate(best[0].code, CONFIG['MUTATION_RATE'])
        return self._generate_advanced_content(goal)

    def _add_library_usage(self, code: str, goal: str) -> str:
        if not self.libraries:
            return code
        other_libs = [lib for lib in self.libraries.values()
                      if lib.is_active and lib.tests_passed > 0 and lib.fitness_score > 70
                      and lib.health_score > 75 and lib.validation_status]
        if not other_libs:
            return code
        same_category = [lib for lib in other_libs if goal in lib.name]
        if same_category and random.random() < 0.3:
            lib = random.choice(same_category)
        else:
            lib = random.choice(other_libs)
        if not lib.exported_functions:
            return code
        func_to_use = random.choice(lib.exported_functions)
        import_line = f"from evolution_libs.{lib.name} import {func_to_use}\n"
        usage_code = f"""
def use_{lib.name}_{func_to_use}(*args, **kwargs):
    \"\"\"Интегрированная функция из {lib.name}\"\"\"
    try:
        result = {func_to_use}(*args, **kwargs)
        return {{
            'success': True,
            'result': result,
            'library': '{lib.name}',
            'function': '{func_to_use}'
        }}
    except Exception as e:
        return {{
            'success': False,
            'error': str(e),
            'library': '{lib.name}',
            'function': '{func_to_use}'
        }}
"""
        lines = code.split('\n')
        insert_pos = 0
        for i, line in enumerate(lines):
            if line.startswith('def ') or line.startswith('class '):
                insert_pos = i
                break
        lines.insert(insert_pos, import_line)
        result = '\n'.join(lines) + usage_code
        
        # Проверяем синтаксис результата
        validator = SyntaxValidator()
        is_valid, fixed_result, errors = validator.validate_and_fix(result, auto_fix=True)
        
        if is_valid:
            lib.times_used += 1
            lib.times_used_as_source += 1
            lib.last_used_generation = self.evolution.state.generation
            self.evolution.state.library_usage_count += 1
            self.evolution.state.cross_category_uses += 1 if goal not in lib.name else 0
            logger.info(f"🔗 Интегрирована {lib.name}.{func_to_use}")
            return fixed_result if fixed_result != result else result
        logger.warning(f"⚠️ Ошибка при интеграции {lib.name}.{func_to_use}")
        return code

    def _load_module(self, name: str, path: str):
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module
        except Exception as e:
            logger.error(f"Ошибка загрузки модуля {name}: {e}")
        return None

    def _test_library(self, module, goal: str) -> tuple:
        if not module:
            return 0, 0
        passed, total = 0, 0
        tests = {
            'ml_ai': ('simple_classifier', ([0.8, 0.9, 0.7],),
                      lambda r: isinstance(r, dict) and 'class' in r),
            'math': ('calculate_stats', [1, 2, 3, 4, 5],
                     lambda r: isinstance(r, dict) and r.get('sum') == 15),
            'algorithms': ('binary_search', ([1, 2, 3, 4, 5], 3),
                           lambda r: r == 2),
            'integration': ('Pipeline', None,
                            lambda r: hasattr(r, 'add_stage')),
        }
        if goal in tests:
            func_name, test_input, validator = tests[goal]
            if hasattr(module, func_name):
                total += 1
                try:
                    if test_input is None:
                        result = getattr(module, func_name)()
                    elif isinstance(test_input, tuple):
                        result = getattr(module, func_name)(*test_input)
                    else:
                        result = getattr(module, func_name)(test_input)
                    if validator(result):
                        passed += 1
                except Exception as e:
                    logger.debug(f"Тест {func_name} не прошёл: {e}")
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and not name.startswith('_'):
                if name not in [tests.get(goal, ('',))[0]]:
                    total += 1
                    try:
                        sig = inspect.signature(obj)
                        args = []
                        for param in sig.parameters.values():
                            if param.default is inspect.Parameter.empty:
                                if param.annotation in (int, float):
                                    args.append(0)
                                elif param.annotation == str:
                                    args.append('')
                                elif param.annotation in (list, List):
                                    args.append([])
                                elif param.annotation in (dict, Dict):
                                    args.append({})
                                else:
                                    args.append(None)
                        result = obj(*args)
                        if result is not None:
                            passed += 1
                    except Exception:
                        pass
        return passed, total

    def _extract_used_libraries(self, code: str) -> List[str]:
        used = []
        for lib_name in self.libraries:
            if f"from evolution_libs.{lib_name}" in code or f"import {lib_name}" in code:
                used.append(lib_name)
        return used

    def _extract_ml_models(self, module) -> List[str]:
        ml_models = []
        if module:
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and any(
                        x in name.lower() for x in ['neural', 'network', 'model', 'classifier']
                ):
                    ml_models.append(name)
        return ml_models

    def get_list(self) -> List[LibraryRecord]:
        return [lib for lib in self.libraries.values() if lib.is_active]

    def get_ml_libraries(self) -> List[LibraryRecord]:
        return [lib for lib in self.libraries.values() if lib.is_active and lib.ml_models]

    def get_stats(self) -> Dict[str, Any]:
        active = [l for l in self.libraries.values() if l.is_active]
        return {
            'total': len(self.libraries),
            'active': len(active),
            'ml_libraries': len(self.get_ml_libraries()),
            'avg_fitness': sum(l.fitness_score for l in active) / max(1, len(active)),
            'avg_health': sum(l.health_score for l in active) / max(1, len(active)),
            'creation_stats': dict(self.creation_stats)
        }

    def update_usage_stats(self, lib_name: str):
        if lib_name in self.libraries:
            self.libraries[lib_name].times_used += 1
            self.libraries[lib_name].last_used_generation = self.evolution.state.generation

    def cleanup_inactive_libraries(self) -> int:
        now = datetime.now()
        to_remove = []
        for name, lib in self.libraries.items():
            if not lib.is_active:
                to_remove.append(name)
                continue
            try:
                created = datetime.fromisoformat(lib.created_at)
                age = (now - created).days
                if age > CONFIG['MAX_LIBRARY_AGE'] and lib.times_used < 1:
                    to_remove.append(name)
            except:
                pass
        for name in to_remove:
            if name in self.libraries:
                del self.libraries[name]
        if to_remove:
            logger.info(f"🧹 Очищено {len(to_remove)} неактивных библиотек")
            self.evolution.state.cleaned_libraries += len(to_remove)
        return len(to_remove)

# ============================================================================
# УЛУЧШЕННЫЙ СОЗДАТЕЛЬ ФУНКЦИЙ (С ВАЛИДАЦИЕЙ)
# ============================================================================
class FunctionCreator:
    def __init__(self, evolution_system):
        self.evolution = evolution_system
        self.code_analyzer = CodeAnalyzer()
        self.functions: Dict[str, FunctionRecord] = {}
        self.creation_stats = defaultdict(int)
        self.syntax_validator = SyntaxValidator()

    @measure_time
    def create_function(self, goal: str, use_evolution: bool = True) -> Optional[FunctionRecord]:
        func_id = random.randint(1000, 9999)
        parent = None
        uses_libs = []
        ml_accuracy = 0.0
        if use_evolution and self.evolution.code_pool.patterns:
            parent = self.evolution.code_pool.select_parent(
                goal, min_quality=CONFIG['MIN_FITNESS_FOR_PARENT']
            )
        if parent and random.random() < CONFIG['CROSSOVER_RATE']:
            other = self.evolution.code_pool.select_parent(
                goal, min_quality=CONFIG['MIN_FITNESS_FOR_PARENT']
            )
            if other:
                code, parents = self.evolution.code_pool.crossover(parent, other)
                code = self.evolution.code_pool.mutate(code, CONFIG['MUTATION_RATE'])
            else:
                code = self.evolution.code_pool.mutate(parent.code, CONFIG['MUTATION_RATE'])
                parents = [parent.id]
        elif parent:
            code = self.evolution.code_pool.mutate(parent.code, CONFIG['MUTATION_RATE'])
            parents = [parent.id]
        else:
            code = self._get_template(goal, func_id)
            parents = []
        if 'List[' in code or 'Dict[' in code or 'Any' in code:
            code = self._add_typing_imports(code)
        
        # Проверяем синтаксис через валидатор
        is_valid, fixed_code, errors = self.syntax_validator.validate_and_fix(code, auto_fix=True)
        if not is_valid:
            self.evolution.state.rejected_syntax_errors += 1
            logger.error(f"❌ Синтаксическая ошибка в функции {func_id}: {errors}")
            return None
        if fixed_code != code:
            logger.debug(f"🔧 Исправлен синтаксис функции {func_id}")
            self.evolution.state.auto_fixed_syntax += 1
            code = fixed_code
        
        try:
            local_ns = {}
            exec(code, {}, local_ns)
            func_names = [k for k in local_ns.keys()
                          if not k.startswith('_') and callable(local_ns[k])]
            if func_names:
                func_name = func_names[0]
                func = local_ns[func_name]
                quality = self.code_analyzer.check_code_quality(code)
                test_result = self._test_function(func, goal)
                if goal == 'ml_ai':
                    ml_accuracy = self._test_ml_accuracy(func)
                fitness = (quality['score'] * 0.3 +
                           (test_result['passed'] / max(1, test_result['total'])) * 40 +
                           ml_accuracy * 30)
                integrity_passed = len(quality.get('broken_functions', [])) == 0
                execution_time = self._measure_execution_time(func)
                record = FunctionRecord(
                    name=func_name, code=code, category=goal,
                    generation=self.evolution.state.generation + 1,
                    tests_passed=test_result['passed'], tests_total=test_result['total'],
                    fitness_score=fitness,
                    parent_pattern_id=parents[0] if parents else None,
                    created_at=datetime.now().isoformat(),
                    is_active=test_result['passed'] > 0,
                    uses_libraries=uses_libs,
                    ml_accuracy=ml_accuracy,
                    error_count=0,
                    validation_status=True,
                    integrity_check_passed=integrity_passed,
                    times_optimized=0,
                    execution_time=execution_time,
                    call_count=0,
                    complexity_score=quality['complexity'],
                    docstring_quality=1.0 if '"""' in code or "'''" in code else 0.0
                )
                self.functions[func_name] = record
                self.creation_stats[goal] += 1
                if test_result['passed'] > 0 and fitness > 65 and quality['score'] >= CONFIG['QUALITY_THRESHOLD']:
                    pattern = CodePattern(
                        id=func_name, code=code, category=goal,
                        fitness_score=fitness, usage_count=0,
                        success_rate=test_result['passed'] / test_result['total'],
                        parent_ids=parents, generation=self.evolution.state.generation,
                        created_at=datetime.now().isoformat(),
                        complexity=quality['complexity'],
                        is_elite=fitness > 85 and quality['score'] > 85,
                        uses_libraries=uses_libs,
                        error_count=0,
                        validation_status=True,
                        quality_score=quality['score'],
                        performance_score=1.0 / (execution_time + 0.1),
                        execution_time=execution_time,
                        syntax_valid=True
                    )
                    self.evolution.code_pool.add_pattern(pattern, self.evolution)
                return record
        except Exception as e:
            logger.error(f"❌ Ошибка при создании функции: {e}")
        return None

    def _add_typing_imports(self, code: str) -> str:
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and line.strip().endswith(':'):
                lines.insert(i + 1, '    from typing import List, Dict, Any, Optional, Tuple, Union')
                break
        return '\n'.join(lines)

    def _get_template(self, goal: str, func_id: int) -> str:
        templates = {
            'math': f'''def math_proc_{func_id}(data):
    """Математическая обработка данных"""
    if not data:
        return {{"error": "Нет данных", "status": "failed"}}
    try:
        result = {{
            "sum": sum(data),
            "mean": sum(data) / len(data) if data else 0,
            "count": len(data),
            "min": min(data),
            "max": max(data)
        }}
        if len(data) > 1:
            result["variance"] = sum((x - result["mean"]) ** 2 for x in data) / len(data)
        return result
    except Exception as e:
        return {{"error": str(e), "status": "failed"}}''',
            'ml_ai': f'''def ml_classify_{func_id}(data):
    """ML классификация данных"""
    if not data:
        return {{"class": "unknown", "confidence": 0, "status": "failed"}}
    try:
        avg = sum(data) / len(data)
        if avg > 0.7:
            result = {{"class": "high", "confidence": avg}}
        elif avg > 0.4:
            result = {{"class": "medium", "confidence": avg}}
        else:
            result = {{"class": "low", "confidence": 1 - avg}}
        result.update({{
            "mean": avg,
            "min": min(data),
            "max": max(data),
            "count": len(data)
        }})
        return result
    except Exception as e:
        return {{"class": "error", "confidence": 0, "error": str(e)}}''',
            'algorithms': f'''def search_{func_id}(data, target):
    """Поиск элемента"""
    try:
        for i, item in enumerate(data):
            if item == target:
                return {{"found": True, "index": i}}
        return {{"found": False, "index": -1}}
    except Exception as e:
        return {{"error": str(e)}}''',
            'integration': f'''def integrate_{func_id}(data, processor):
    """Интеграция с процессором"""
    try:
        if hasattr(processor, 'process'):
            return processor.process(data)
        return processor(data)
    except Exception as e:
        return {{"error": str(e)}}'''
        }
        return templates.get(goal, templates['math'])

    def _test_function(self, func, category: str) -> Dict:
        result = {'passed': 0, 'total': 0}
        try:
            result['total'] = 1
            tests = {
                'math': (lambda: func([1, 2, 3, 4, 5]),
                         lambda r: isinstance(r, dict) and r.get('sum') == 15),
                'ml_ai': (lambda: func([0.8, 0.9, 0.7]),
                          lambda r: isinstance(r, dict) and 'class' in r),
                'algorithms': (lambda: func([1, 2, 3, 4, 5], 3),
                               lambda r: isinstance(r, dict) and r.get('found', False)),
                'integration': (lambda: func("test", lambda x: x.upper()),
                                lambda r: r == "TEST" or isinstance(r, dict))
            }
            if category in tests:
                run_test, validate = tests[category]
                out = run_test()
                if validate(out):
                    result['passed'] += 1
            else:
                try:
                    out = func([1, 2, 3])
                    if isinstance(out, (dict, str, int, float, list)):
                        result['passed'] = 1
                except:
                    pass
        except Exception as e:
            logger.debug(f"Тест не прошёл: {e}")
        return result

    def _test_ml_accuracy(self, func) -> float:
        try:
            test_cases = [
                ([0.1, 0.2, 0.1], 'low'),
                ([0.8, 0.9, 0.7], 'high'),
                ([0.4, 0.5, 0.4], 'medium')
            ]
            correct = 0
            for data, expected in test_cases:
                result = func(data)
                if isinstance(result, dict):
                    pred = result.get('class', '')
                    if pred == expected or expected in str(pred).lower():
                        correct += 1
                    elif expected == 'medium' and 'medium' in str(pred).lower():
                        correct += 1
            return correct / len(test_cases)
        except Exception:
            return 0.0

    def _measure_execution_time(self, func) -> float:
        try:
            start = time.perf_counter()
            func([1, 2, 3])
            return time.perf_counter() - start
        except:
            return 1.0

    def get_list(self) -> List[FunctionRecord]:
        return [f for f in self.functions.values() if f.is_active]

    def get_stats(self) -> Dict[str, Any]:
        active = [f for f in self.functions.values() if f.is_active]
        return {
            'total': len(self.functions),
            'active': len(active),
            'avg_fitness': sum(f.fitness_score for f in active) / max(1, len(active)),
            'avg_accuracy': sum(f.ml_accuracy for f in active) / max(1, len(active)),
            'creation_stats': dict(self.creation_stats)
        }

# ============================================================================
# МОДУЛЬ ДЛЯ ИМИТАЦИИ ПОИСКА В ИНТЕРНЕТЕ
# ============================================================================
class WebResearch:
    """Имитирует поиск в интернете для получения новых идей."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.topics = self._load_topics()
            self.cache = {}

    def _load_topics(self) -> Dict[str, List[Dict]]:
        """Загружает базу знаний по различным темам."""
        return {
            'algorithms': [
                {'name': 'Быстрая сортировка (quick sort)', 'complexity': 5, 'tags': ['sort', 'divide_conquer']},
                {'name': 'Алгоритм Дейкстры (dijkstra)', 'complexity': 7, 'tags': ['graph', 'shortest_path']},
                {'name': 'Поиск в глубину (dfs)', 'complexity': 4, 'tags': ['graph', 'traversal']},
                {'name': 'Динамическое программирование (dp)', 'complexity': 9, 'tags': ['optimization']},
                {'name': 'Хеш-таблицы (hash tables)', 'complexity': 3, 'tags': ['data_structure']},
            ],
            'ml_ai': [
                {'name': 'Трансформеры (transformers)', 'complexity': 10, 'tags': ['nlp', 'attention']},
                {'name': 'Сверточные сети (cnn)', 'complexity': 8, 'tags': ['vision', 'deep_learning']},
                {'name': 'Градиентный бустинг (xgboost)', 'complexity': 7, 'tags': ['ensemble', 'tabular']},
                {'name': 'Автокодировщики (autoencoders)', 'complexity': 8, 'tags': ['unsupervised']},
                {'name': 'Обучение с подкреплением (rl)', 'complexity': 9, 'tags': ['agent']},
            ],
            'integration': [
                {'name': 'Шина данных (message bus)', 'complexity': 6, 'tags': ['messaging', 'decoupling']},
                {'name': 'API-шлюз (api gateway)', 'complexity': 7, 'tags': ['microservices']},
                {'name': 'Адаптер (adapter pattern)', 'complexity': 3, 'tags': ['design_pattern']},
                {'name': 'Брокер сообщений (message broker)', 'complexity': 8, 'tags': ['rabbitmq', 'kafka']},
            ],
            'database': [
                {'name': 'Индексирование (b-tree)', 'complexity': 7, 'tags': ['performance']},
                {'name': 'Репликация (master-slave)', 'complexity': 6, 'tags': ['scalability']},
                {'name': 'Шардинг (sharding)', 'complexity': 8, 'tags': ['scalability']},
                {'name': 'Транзакции (acid)', 'complexity': 5, 'tags': ['consistency']},
            ],
            'security': [
                {'name': 'Шифрование (aes)', 'complexity': 6, 'tags': ['cryptography']},
                {'name': 'JWT (json web token)', 'complexity': 4, 'tags': ['authentication']},
                {'name': 'OAuth 2.0', 'complexity': 7, 'tags': ['authorization']},
                {'name': 'SQL-инъекции (prevention)', 'complexity': 3, 'tags': ['vulnerability']},
            ],
            'visualization': [
                {'name': 'Интерактивные дашборды', 'complexity': 6, 'tags': ['dashboard', 'ui']},
                {'name': '3D визуализация', 'complexity': 8, 'tags': ['3d', 'graphics']},
                {'name': 'Визуализация графов', 'complexity': 7, 'tags': ['graph', 'network']},
                {'name': 'Тепловые карты', 'complexity': 4, 'tags': ['heatmap', 'density']},
            ]
        }

    def search_idea(self, category: str) -> Optional[Dict]:
        """Ищет идею для заданной категории."""
        topics = self.topics.get(category, [])
        if not topics:
            return None
        idea = random.choice(topics).copy()
        idea['source'] = 'web_research'
        return idea

    def get_inspiration(self, current_progress: Dict[str, float]) -> str:
        """Возвращает новую цель для эволюции на основе прогресса и веб-знаний.
        Всегда возвращает существующую цель.
        """
        # Фильтруем прогресс, оставляя только существующие цели
        valid_progress = {}
        for k, v in current_progress.items():
            if k in EVOLUTION_GOALS:
                valid_progress[k] = v
        
        if not valid_progress:
            return 'ml_ai'  # fallback
        
        # Проверяем, есть ли категории на 100%
        max_cats = [g for g, p in valid_progress.items() if p >= 1.0]
        if max_cats and len(max_cats) >= 3 and random.random() < 0.3:
            logger.info(f"🎯 Много категорий на 100%, ищу новую цель")
            all_cats = set(EVOLUTION_GOALS.keys())
            achieved = set(max_cats)
            remaining = all_cats - achieved
            if remaining:
                return random.choice(list(remaining))
        
        # Если есть очень слабые категории
        weak_cats = [g for g, p in valid_progress.items() if p < CONFIG['WEAK_CATEGORY_THRESHOLD']]
        if weak_cats:
            target_cat = random.choice(weak_cats)
            idea = self.search_idea(target_cat)
            if idea:
                logger.info(f"🌐 WebResearch: Найдена идея '{idea['name']}' для усиления {target_cat}")
            return target_cat

        # Если всё хорошо, ищем новую комбинацию
        if random.random() < 0.3:
            new_cat = random.choice(list(EVOLUTION_GOALS.keys()))
            idea = self.search_idea(new_cat)
            if idea:
                logger.info(f"🌐 WebResearch: Найдена новая идея '{idea['name']}' для {new_cat}")
            return new_cat

        # По умолчанию возвращаем категорию с наименьшим прогрессом
        return min(valid_progress, key=valid_progress.get)

# ============================================================================
# ОПТИМИЗИРОВАННАЯ СИСТЕМА ЭВОЛЮЦИИ (УЛУЧШЕННАЯ С ВАЛИДАЦИЕЙ)
# ============================================================================
class EvolutionSystem:
    def __init__(self):
        self.running = True
        self.state = EvolutionState()
        self.state.start_time = datetime.now().isoformat()
        self.code_analyzer = CodeAnalyzer()
        self.code_pool = GeneticCodePool(CONFIG['MAX_CODE_POOL_SIZE'])
        self.code_pool.set_code_analyzer(self.code_analyzer)
        self.code_pool.evolution = self
        self.memory_manager = MemoryManager()
        self.ml_predictor = MLPredictor(self)
        self.dependency_creator = DependencyCreator(self)
        self.library_creator = LibraryCreator(self)
        self.function_creator = FunctionCreator(self)
        self.meta_evolution = MetaEvolutionEngine(self)
        self.health_manager = HealthManager(self)
        self.self_evolution = SelfEvolutionEngine(self)
        self.goal_unlocker = GoalUnlocker(self)
        self.web_research = WebResearch()
        self.visualizer = EvolutionVisualizer()
        self.report_exporter = ReportExporter(self)
        
        # НОВЫЕ МОДУЛИ
        self.code_compactor = CodeCompactor(self)
        self.meta_injector = MetaKnowledgeInjector(self)
        self.advanced_healer = AdvancedSelfHealer(self)
        self.adaptive_balancer = AdaptiveBalancer(self)
        self.dynamic_goal_creator = DynamicGoalCreator(self)
        
        pattern_recognizer = PatternRecognizer()
        self.code_analyzer.set_ml_predictor(self.ml_predictor)
        self.code_analyzer.set_pattern_recognizer(pattern_recognizer)
        self.code_analyzer.set_dependency_creator(self.dependency_creator)
        
        self.code_pool.set_compactor(self.code_compactor)
        self.code_pool.set_healer(self.advanced_healer)
        
        self.last_mut = time.time()
        self.last_cleanup = time.time()
        self.last_health_check = time.time()
        self.last_unused_cleanup = time.time()
        self.last_balance_check = time.time()
        self.last_save = time.time()
        self.last_self_evolution = time.time()
        self.last_compaction = time.time()
        self.last_meta_injection = time.time()
        self.last_goal_creation = time.time()
        
        self.mutation_queue = asyncio.Queue()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.setup_dirs()
        self.load_state()
        if not self.library_creator.libraries:
            self._initialize_base_libraries()
        logger.info("🚀 Система v32.0 запущена | КВАНТОВЫЙ СКАЧОК + ИНТЕЛЛЕКТ + СИНТАКСИЧЕСКАЯ ЧИСТОТА")

    def setup_dirs(self):
        for d in [CONFIG['GENERATIONS_DIR'], CONFIG['BACKUP_DIR'],
                  CONFIG['LIBRARIES_DIR'], CONFIG['MODELS_DIR'],
                  CONFIG['REPORTS_DIR']]:
            Path(d).mkdir(exist_ok=True)

    def _initialize_base_libraries(self):
        logger.info("🌱 Создание начальных библиотек...")
        for goal in BASE_EVOLUTION_GOALS.keys():
            lib_name = self.library_creator.create_library(goal, use_evolution=False)
            if lib_name:
                logger.info(f"   ✅ {BASE_EVOLUTION_GOALS[goal]['icon']} {goal}")
            time.sleep(0.1)

    def load_state(self):
        try:
            if os.path.exists(CONFIG['STATE_FILE']):
                with open(CONFIG['STATE_FILE'], 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.state.generation = data.get('generation', 0)
                self.state.best_fitness = data.get('best_fitness', 0)
                self.state.fitness_history = data.get('fitness_history', [])
                self.state.goals_progress = data.get('goals_progress',
                                                     {g: 0.0 for g in BASE_EVOLUTION_GOALS.keys()})
                self.state.unlocked_goals = set(data.get('unlocked_goals', list(BASE_EVOLUTION_GOALS.keys())))
                for field in ['library_usage_count', 'ml_models_created', 'ml_predictions_made',
                              'cross_category_uses', 'meta_evolution_count', 'meta_evolution_success',
                              'self_evolution_count', 'self_evolution_success',
                              'fixed_syntax_errors', 'cleaned_libraries', 'removed_broken_libraries',
                              'healed_libraries', 'added_imports', 'removed_unused_libraries',
                              'avg_health_score', 'removed_duplicate_imports', 'fixed_broken_functions',
                              'removed_dead_code', 'healing_attempts', 'successful_healing',
                              'balance_adjustments', 'patterns_merged', 'functions_optimized',
                              'proactive_heals', 'avg_complexity', 'innovation_score', 'performance_score',
                              'created_dependencies', 'custom_goals_created', 'meta_injections',
                              'compactions_performed', 'self_healing_refactors', 'adaptive_weights_applied',
                              'stagnation_recovery', 'rejected_syntax_errors', 'auto_fixed_syntax']:
                    if field in data:
                        setattr(self.state, field, data[field])
                logger.info(f"📂 Загружено: поколение {self.state.generation}")
                logger.info(f"🔓 Разблокировано целей: {len(self.state.unlocked_goals)}")
        except Exception as e:
            logger.error(f"Ошибка загрузки состояния: {e}")

    def save_state(self):
        try:
            self.state.code_pool_size = len(self.code_pool.patterns)
            self.state.elite_patterns = len(self.code_pool.elite_patterns)
            self.state.total_functions = len(self.function_creator.functions)
            self.state.total_classes = sum(p.class_count for p in self.code_pool.patterns.values())
            health_scores = [lib.health_score for lib in self.library_creator.libraries.values() if lib.is_active]
            self.state.avg_health_score = sum(health_scores) / max(1, len(health_scores))
            complexities = [p.complexity for p in self.code_pool.patterns.values()]
            self.state.avg_complexity = sum(complexities) / max(1, len(complexities))
            innovations = [p.innovation_score for p in self.code_pool.patterns.values()]
            self.state.innovation_score = sum(innovations) / max(1, len(innovations))
            
            global EVOLUTION_GOALS
            for goal_id in self.state.unlocked_goals:
                if goal_id in LOCKED_GOALS and goal_id not in EVOLUTION_GOALS:
                    goal_info = LOCKED_GOALS[goal_id]
                    EVOLUTION_GOALS[goal_id] = {
                        'name': goal_info['name'],
                        'weight': goal_info['weight'],
                        'icon': goal_info['icon'],
                        'priority': goal_info['priority'],
                        'unlocked': True,
                        'category': goal_info.get('category', 'advanced')
                    }
            
            data = {
                'generation': self.state.generation,
                'best_fitness': self.state.best_fitness,
                'current_fitness': self.state.current_fitness,
                'mutation_count': self.state.mutation_count,
                'successful_mutations': self.state.successful_mutations,
                'failed_mutations': self.state.failed_mutations,
                'fitness_history': self.state.fitness_history[-200:],
                'goals_progress': self.state.goals_progress,
                'unlocked_goals': list(self.state.unlocked_goals),
                'code_pool_size': self.state.code_pool_size,
                'elite_patterns': self.state.elite_patterns,
                'total_functions': self.state.total_functions,
                'total_classes': self.state.total_classes,
                'library_usage_count': self.state.library_usage_count,
                'ml_models_created': self.state.ml_models_created,
                'ml_predictions_made': self.state.ml_predictions_made,
                'ml_accuracy_avg': self.state.ml_accuracy_avg,
                'cross_category_uses': self.state.cross_category_uses,
                'meta_evolution_count': self.state.meta_evolution_count,
                'meta_evolution_success': self.state.meta_evolution_success,
                'self_evolution_count': self.state.self_evolution_count,
                'self_evolution_success': self.state.self_evolution_success,
                'fixed_syntax_errors': self.state.fixed_syntax_errors,
                'cleaned_libraries': self.state.cleaned_libraries,
                'removed_broken_libraries': self.state.removed_broken_libraries,
                'healed_libraries': self.state.healed_libraries,
                'added_imports': self.state.added_imports,
                'removed_unused_libraries': self.state.removed_unused_libraries,
                'removed_duplicate_imports': self.state.removed_duplicate_imports,
                'fixed_broken_functions': self.state.fixed_broken_functions,
                'removed_dead_code': self.state.removed_dead_code,
                'healing_attempts': self.state.healing_attempts,
                'successful_healing': self.state.successful_healing,
                'balance_adjustments': self.state.balance_adjustments,
                'patterns_merged': self.state.patterns_merged,
                'functions_optimized': self.state.functions_optimized,
                'proactive_heals': self.state.proactive_heals,
                'avg_health_score': self.state.avg_health_score,
                'avg_complexity': self.state.avg_complexity,
                'innovation_score': self.state.innovation_score,
                'performance_score': self.state.performance_score,
                'created_dependencies': self.state.created_dependencies,
                'custom_goals_created': self.state.custom_goals_created,
                'meta_injections': self.state.meta_injections,
                'compactions_performed': self.state.compactions_performed,
                'self_healing_refactors': self.state.self_healing_refactors,
                'adaptive_weights_applied': self.state.adaptive_weights_applied,
                'stagnation_recovery': self.state.stagnation_recovery,
                'mutation_weights': self.state.mutation_weights,
                'rejected_syntax_errors': self.state.rejected_syntax_errors,
                'auto_fixed_syntax': self.state.auto_fixed_syntax,
                'last_save': datetime.now().isoformat()
            }
            with open(CONFIG['STATE_FILE'], 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.code_pool.save_pool()
            self.meta_evolution.save_meta_history()
        except Exception as e:
            logger.error(f"Ошибка сохранения состояния: {e}")

    def select_goal(self) -> str:
        """Выбирает цель для мутации с проверкой существования."""
        goal = self.web_research.get_inspiration(self.state.goals_progress)
        
        # Проверяем, существует ли выбранная цель
        if goal not in EVOLUTION_GOALS:
            logger.warning(f"Цель {goal} не найдена в EVOLUTION_GOALS, выбираем из доступных")
            # Выбираем случайную доступную цель
            available_goals = list(EVOLUTION_GOALS.keys())
            if available_goals:
                selected = random.choice(available_goals)
                logger.info(f"Выбрана альтернативная цель: {selected}")
                return selected
            logger.error("Нет доступных целей! Используем ml_ai")
            return 'ml_ai'  # fallback
        
        return goal

    @measure_time
    def mutate(self) -> bool:
        self.state.mutation_count += 1
        # Выбираем тип мутации на основе адаптивной балансировки
        mutation_type = self.adaptive_balancer.select_mutation_type()
        
        # Если нужно, создаём новую цель
        if mutation_type == 'create_goal' and CONFIG['DYNAMIC_GOAL_CREATION']:
            if time.time() - self.last_goal_creation > 60:  # Не чаще раза в минуту
                new_goal = self.dynamic_goal_creator.create_new_goal()
                if new_goal:
                    self.last_goal_creation = time.time()
                    goal = new_goal
                else:
                    goal = self.select_goal()
            else:
                goal = self.select_goal()
        else:
            goal = self.select_goal()
        
        # Дополнительная проверка существования цели
        if goal not in EVOLUTION_GOALS:
            logger.error(f"❌ Цель {goal} не существует в EVOLUTION_GOALS, используем ml_ai")
            goal = 'ml_ai'
            self.state.consecutive_failures += 1
        else:
            self.state.consecutive_failures = 0
        
        self.state.last_goal = goal
        ml_pred = self.ml_predictor.predict_mutation_success("", goal)
        
        # Безопасное получение имени цели
        goal_name = EVOLUTION_GOALS[goal]['name'] if goal in EVOLUTION_GOALS else goal
        logger.info(f"🎯 Цель: {goal_name} (ML: {ml_pred:.2f}, тип: {mutation_type})")
        
        success = False
        quality = 0
        
        # Проверяем, не слишком ли много последовательных ошибок
        if self.state.consecutive_failures >= self.state.max_consecutive_failures:
            logger.warning(f"⚠️ Слишком много последовательных ошибок ({self.state.consecutive_failures}), принудительное исцеление")
            mutation_type = 'self_heal'
            self.state.consecutive_failures = 0
        
        # Выполняем мутацию в зависимости от типа
        if mutation_type == 'add_feature' or mutation_type == 'add_library':
            if random.random() < 0.7:
                lib = self.library_creator.create_library(goal, use_evolution=True)
                if lib:
                    rec = self.library_creator.libraries.get(lib)
                    if rec and rec.tests_passed > 0:
                        success = True
                        quality = rec.fitness_score
                        logger.info(f"✅ Библиотека: {rec.tests_passed}/{rec.tests_total} (fitness: {quality:.0f})")
                        self._update_progress(goal, True, quality)
            
            if random.random() < 0.6:
                func = self.function_creator.create_function(goal, use_evolution=True)
                if func and func.is_active:
                    success = True
                    quality = max(quality, func.fitness_score)
                    logger.info(f"✅ Функция: {func.name} (fitness: {func.fitness_score:.0f})")
                    self._update_progress(goal, True, quality)
        
        elif mutation_type == 'mutate_code':
            # Обычная мутация кода
            if random.random() < 0.6:
                func = self.function_creator.create_function(goal, use_evolution=True)
                if func and func.is_active:
                    success = True
                    quality = func.fitness_score
                    logger.info(f"✅ Функция: {func.name} (fitness: {func.fitness_score:.0f})")
                    self._update_progress(goal, True, quality)
        
        elif mutation_type == 'code_compaction' and CONFIG['CODE_COMPACTION_ENABLED']:
            # Сжатие кода застойных паттернов
            stagnant = self.code_pool.get_stagnant_patterns(3)
            for pattern in stagnant:
                compacted_code, stats = self.code_compactor.compact_code(pattern.code, pattern.id)
                if stats['dead_branches'] + stats['duplicate_lines'] + stats['redundant_assignments'] > 0:
                    # Создаём новый паттерн на основе сжатого
                    quality_check = self.code_analyzer.check_code_quality(compacted_code)
                    new_pattern = CodePattern(
                        id=f"{pattern.id}_compacted_{int(time.time())}",
                        code=compacted_code,
                        category=pattern.category,
                        fitness_score=pattern.fitness_score * 1.02,  # Небольшой бонус
                        usage_count=0,
                        success_rate=pattern.success_rate,
                        parent_ids=[pattern.id],
                        generation=self.state.generation,
                        created_at=datetime.now().isoformat(),
                        complexity=quality_check['complexity'],
                        is_elite=pattern.is_elite,
                        uses_libraries=pattern.uses_libraries,
                        validation_status=True,
                        quality_score=quality_check['score'],
                        innovation_score=pattern.innovation_score + 0.05,
                        dead_code_removed=stats['dead_branches'] + stats['duplicate_lines'],
                        syntax_valid=True
                    )
                    if self.code_pool.add_pattern(new_pattern, self):
                        success = True
                        self.state.compactions_performed += 1
                        self.code_pool.mark_improved(pattern.id)
                        logger.info(f"🧹 СЖАТИЕ: {pattern.id} -> {new_pattern.id} (удалено {stats['dead_branches']} веток, {stats['duplicate_lines']} дублей)")
        
        elif mutation_type == 'self_heal' and CONFIG['SELF_HEALING_REFACTOR']:
            # Продвинутое самоисцеление
            to_heal = self.code_pool.get_stagnant_patterns(2)
            for pattern in to_heal:
                healed, new_pattern, changes = self.advanced_healer.heal_pattern(pattern)
                if healed and new_pattern:
                    if self.code_pool.add_pattern(new_pattern, self):
                        success = True
                        self.state.self_healing_refactors += 1
                        self.code_pool.mark_improved(pattern.id)
                        logger.info(f"💊 ИСЦЕЛЕНИЕ: {pattern.id} -> {new_pattern.id} ({', '.join(changes[:2])})")
        
        elif mutation_type == 'meta_inject' and CONFIG['META_KNOWLEDGE_INJECTION']:
            # Внедрение мета-знаний
            if time.time() - self.last_meta_injection > 30:  # Не чаще раза в 30 секунд
                if self.meta_injector.inject_knowledge():
                    success = True
                    self.last_meta_injection = time.time()
        
        # Мета-эволюция всё равно может произойти
        if self.meta_evolution.should_trigger_meta_evolution():
            meta_record = self.meta_evolution.create_meta_evolution()
            if meta_record:
                logger.info(f"🆕 META: {meta_record.id} (fitness: {meta_record.fitness_score:.0f})")
        
        # Проверяем разблокировку новых целей
        if self.state.generation % 5 == 0:
            new_goals = self.goal_unlocker.check_unlocks()
            for new_goal in new_goals:
                if self.goal_unlocker.unlock_goal(new_goal):
                    logger.info(f"🎉 Разблокирована новая цель: {new_goal}")
        
        # Проверяем, нужно ли эволюционировать самой системе
        if self.self_evolution.should_self_evolve():
            if time.time() - self.last_self_evolution > 30:
                self_record = self.self_evolution.evolve_self()
                if self_record:
                    self.last_self_evolution = time.time()
        
        # Проверка здоровья
        if time.time() - self.last_health_check > CONFIG['HEALTH_CHECK_INTERVAL'] * 60:
            removed, healed = self.health_manager.cleanup_broken_libraries()
            if removed > 0 or healed > 0:
                self.state.removed_broken_libraries += removed
                self.state.healed_libraries += healed
                logger.info(f"🏥 Здоровье: удалено {removed}, исцелено {healed}")
            proactive = self.health_manager.process_proactive_queue()
            if proactive > 0:
                logger.info(f"🔮 Проактивное исцеление: {proactive}")
            self.last_health_check = time.time()
        
        # Очистка неиспользуемых
        if time.time() - self.last_unused_cleanup > CONFIG['CLEANUP_INTERVAL'] * 20:
            removed = self.health_manager.cleanup_unused_libraries()
            if removed > 0:
                logger.info(f"🗑️ Очистка: удалено {removed} неиспользуемых")
            self.last_unused_cleanup = time.time()
        
        # Адаптивная балансировка весов
        if time.time() - self.last_balance_check > 30 and CONFIG['ADAPTIVE_MUTATION_WEIGHTS']:
            if self.adaptive_balancer.adjust_weights():
                self.last_balance_check = time.time()
        
        if success:
            self.state.generation += 1
            self.state.successful_mutations += 1
            self.state.consecutive_failures = 0
        else:
            self.state.failed_mutations += 1
            self.state.consecutive_failures += 1
            self._update_progress(goal, False)
        
        fitness = self._calculate_fitness()
        self.state.fitness_history.append(fitness)
        self.state.current_fitness = fitness
        
        if fitness > self.state.best_fitness:
            improvement = fitness - self.state.best_fitness
            self.state.best_fitness = fitness
            logger.info(f"🏆 НОВЫЙ РЕКОРД! Fitness: {fitness:.0f} (+{improvement:.0f})")
            
            # Обновляем прогресс динамических целей
            self.dynamic_goal_creator.update_goal_progress('improve_ml', improvement / 1000)
        
        if self.state.generation % 10 == 0:
            self.save_state()
            self.report_exporter.export_auto()
        
        if time.time() - self.last_cleanup > CONFIG['CLEANUP_INTERVAL'] * 60:
            cleaned = self.code_pool.cleanup_old_patterns()
            self.state.cleaned_libraries += cleaned
            self.last_cleanup = time.time()
        
        return success

    def _update_progress(self, goal: str, success: bool, quality: float = 0):
        """Обновляет прогресс по цели с проверкой существования."""
        # Проверяем существование цели в прогрессе
        if goal not in self.state.goals_progress:
            logger.debug(f"Цель {goal} не найдена в прогрессе, пропускаем обновление")
            return
        
        # Проверяем существование цели в EVOLUTION_GOALS
        if goal not in EVOLUTION_GOALS:
            logger.debug(f"Цель {goal} не найдена в EVOLUTION_GOALS, пропускаем обновление")
            return
        
        if success:
            # Базовое увеличение
            inc = 0.02 + (quality / 100) * 0.08
            
            # Бонус для ML/AI
            if goal == 'ml_ai':
                inc *= 1.5
            # Бонус для слабых категорий
            elif self.state.goals_progress[goal] < CONFIG['WEAK_CATEGORY_THRESHOLD']:
                inc *= 1.3
            
            # Применяем увеличение
            old_value = self.state.goals_progress[goal]
            self.state.goals_progress[goal] = min(1.0, old_value + inc)
            
            logger.debug(f"Прогресс по цели {goal}: {old_value:.2f} -> {self.state.goals_progress[goal]:.2f} (+{inc:.3f})")
            
            # Обновляем динамические цели только если они существуют
            if hasattr(self, 'dynamic_goal_creator') and self.dynamic_goal_creator:
                self.dynamic_goal_creator.update_goal_progress(goal, inc)
        else:
            # Небольшое уменьшение при неудаче
            old_value = self.state.goals_progress[goal]
            self.state.goals_progress[goal] = max(0.0, old_value - 0.01)
            logger.debug(f"Прогресс по цели {goal}: {old_value:.2f} -> {self.state.goals_progress[goal]:.2f} (-0.01)")

    def _calculate_fitness(self) -> float:
        func_fit = sum(f.fitness_score for f in self.function_creator.functions.values() if f.is_active)
        lib_fit = sum(l.fitness_score for l in self.library_creator.libraries.values() if l.is_active)
        goal_fit = sum(self.state.goals_progress.values()) * 100
        elite_bonus = len(self.code_pool.elite_patterns) * 50
        categories = set(f.category for f in self.function_creator.functions.values() if f.is_active)
        categories.update(l.category for l in self.code_pool.patterns.values())
        diversity = len(categories) * 30
        lib_usage_bonus = self.state.library_usage_count * 10
        ml_bonus = self.state.ml_models_created * 40 + self.state.ml_predictions_made * 5
        cross_bonus = self.state.cross_category_uses * 20
        meta_bonus = self.state.meta_evolution_success * 100
        self_bonus = self.state.self_evolution_success * 200
        fix_bonus = self.state.fixed_syntax_errors * 15
        health_bonus = self.state.avg_health_score * 5
        healing_bonus = self.state.healed_libraries * 50
        import_bonus = self.state.added_imports * 10
        cleanup_bonus = self.state.removed_unused_libraries * 20
        duplicate_bonus = self.state.removed_duplicate_imports * 5
        function_bonus = self.state.fixed_broken_functions * 30
        dead_code_bonus = self.state.removed_dead_code * 10
        healing_effort_bonus = self.state.successful_healing * 100
        balance_bonus = self.state.balance_adjustments * 10
        merge_bonus = self.state.patterns_merged * 50
        optimize_bonus = self.state.functions_optimized * 20
        proactive_bonus = self.state.proactive_heals * 30
        innovation_bonus = self.state.innovation_score * 200
        complexity_bonus = self.state.avg_complexity * 10
        dependency_bonus = self.state.created_dependencies * 50
        
        # НОВЫЕ БОНУСЫ
        custom_goal_bonus = self.state.custom_goals_created * 150
        meta_injection_bonus = self.state.meta_injections * 100
        compaction_bonus = self.state.compactions_performed * 80
        self_heal_refactor_bonus = self.state.self_healing_refactors * 120
        adaptive_weight_bonus = self.state.adaptive_weights_applied * 50
        stagnation_recovery_bonus = self.state.stagnation_recovery * 200
        syntax_quality_bonus = (self.state.rejected_syntax_errors * -50) + (self.state.auto_fixed_syntax * 30)
        
        total = (func_fit + lib_fit + goal_fit + elite_bonus + diversity +
                 lib_usage_bonus + ml_bonus + cross_bonus + meta_bonus + self_bonus +
                 fix_bonus + health_bonus + healing_bonus + import_bonus +
                 cleanup_bonus + duplicate_bonus + function_bonus + dead_code_bonus +
                 healing_effort_bonus + balance_bonus + merge_bonus + optimize_bonus +
                 proactive_bonus + innovation_bonus + complexity_bonus + dependency_bonus +
                 custom_goal_bonus + meta_injection_bonus + compaction_bonus +
                 self_heal_refactor_bonus + adaptive_weight_bonus + stagnation_recovery_bonus +
                 syntax_quality_bonus)
        return total

    def evolution_cycle(self):
        now = time.time()
        self.visualizer.display(
            self.state,
            self.library_creator.get_list(),
            self.function_creator.get_list()
        )
        if now - self.last_mut > CONFIG['MUTATION_INTERVAL']:
            logger.info("🔄 Мутация...")
            self.mutate()
            self.last_mut = now

    async def async_evolution_cycle(self):
        while self.running:
            try:
                self.evolution_cycle()
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"❌ Ошибка: {e}")
                traceback.print_exc()
                await asyncio.sleep(5)

    def background_worker(self):
        asyncio.run(self.async_evolution_cycle())

    def start(self):
        thread = threading.Thread(target=self.background_worker, daemon=True)
        thread.start()
        logger.info("🚀 Эволюция запущена")

    def run(self):
        self.start()
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self):
        logger.info("👋 Остановка...")
        removed, healed = self.health_manager.cleanup_broken_libraries()
        unused = self.health_manager.cleanup_unused_libraries()
        proactive = self.health_manager.process_proactive_queue()
        if removed > 0 or healed > 0 or unused > 0 or proactive > 0:
            logger.info(f"🏥 Финальная проверка: удалено {removed}, исцелено {healed}, неиспользуемых {unused}, проактивно {proactive}")
        self.save_state()
        self.report_exporter.export_json_report()
        self.executor.shutdown()
        self.memory_manager.clear()
        self.running = False
        logger.info("✅ Завершено")

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ ВИЗУАЛИЗАТОР (УЛУЧШЕННЫЙ)
# ============================================================================
class EvolutionVisualizer:
    def __init__(self):
        self.last = 0
        self._lock = threading.Lock()
        self.cache = {}

    def clear(self):
        print('\033[H\033[J', end='')
        sys.stdout.flush()

    def bar(self, val: float, w: int = 20, label: str = "") -> str:
        f = int(val * w)
        if val >= 0.8:
            color = '\033[92m'
        elif val >= 0.5:
            color = '\033[93m'
        else:
            color = '\033[91m'
        bar_str = f"{color}[{'█' * f}{'░' * (w - f)}]\033[0m {val * 100:.1f}%"
        if label:
            bar_str = f"{label} {bar_str}"
        return bar_str

    def health_bar(self, val: float, w: int = 10) -> str:
        f = int(val / 10)
        if val >= 80:
            color = '\033[92m'
        elif val >= 50:
            color = '\033[93m'
        else:
            color = '\033[91m'
        return f"{color}[{'█' * f}{'░' * (w - f)}]\033[0m {val:.1f}%"

    def display(self, state: EvolutionState, libs, funcs):
        with self._lock:
            if time.time() - self.last < CONFIG['VISUAL_UPDATE_INTERVAL']:
                return
            self.last = time.time()
            self.clear()
            print("=" * 120)
            print("🤖 САМОЭВОЛЮЦИЯ v32.0 | КВАНТОВЫЙ СКАЧОК + ИНТЕЛЛЕКТ + СИНТАКСИЧЕСКАЯ ЧИСТОТА")
            print("=" * 120)
            elapsed = datetime.now() - datetime.fromisoformat(state.start_time) if state.start_time else timedelta(0)
            print(f"⏰ {datetime.now().strftime('%H:%M:%S')} | Поколение: {state.generation} | Время: {elapsed}")
            print("-" * 120)
            print("📈 FITNESS:")
            print(f"   Текущий: {state.current_fitness:.0f} | Лучший: {state.best_fitness:.0f}")
            if state.fitness_history:
                avg = sum(state.fitness_history[-10:]) / min(len(state.fitness_history), 10)
                print(f"   Средний (10): {avg:.0f}")
            print()
            print("🏥 ЗДОРОВЬЕ:")
            print(f"   Среднее: {self.health_bar(state.avg_health_score, 15)}")
            print(f"   Удалено битых: {state.removed_broken_libraries} | Исцелено: {state.healed_libraries}")
            print(f"   Попыток исцеления: {state.healing_attempts} | Успешных: {state.successful_healing}")
            print(f"   🔮 Проактивных: {state.proactive_heals}")
            print(f"   🗑️ Неиспользуемых: {state.removed_unused_libraries}")
            print(f"   🔁 Дублирующихся импортов: {state.removed_duplicate_imports}")
            print(f"   🔧 Сломанных функций: {state.fixed_broken_functions}")
            print(f"   💀 Мёртвого кода: {state.removed_dead_code}")
            print(f"   ➕ Добавлено импортов: {state.added_imports}")
            print(f"   ⚖️ Балансировок: {state.balance_adjustments}")
            print(f"   🔗 Слияний: {state.patterns_merged}")
            print(f"   ⚡ Оптимизаций: {state.functions_optimized}")
            print(f"   📦 Создано зависимостей: {state.created_dependencies}")
            print()
            print("🔧 СИНТАКСИЧЕСКАЯ СТАТИСТИКА:")
            print(f"   ❌ Отклонено ошибок: {state.rejected_syntax_errors}")
            print(f"   🔧 Автоисправлено: {state.auto_fixed_syntax}")
            print(f"   ⚠️ Последовательных ошибок: {state.consecutive_failures}/{state.max_consecutive_failures}")
            print()
            print("🧹 НОВЫЕ УЛУЧШЕНИЯ:")
            print(f"   📦 Динамических целей: {state.custom_goals_created}")
            print(f"   🔄 Мета-инъекций: {state.meta_injections}")
            print(f"   🧹 Сжатий кода: {state.compactions_performed}")
            print(f"   💊 Самоисцелений: {state.self_healing_refactors}")
            print(f"   ⚖️ Адаптивных балансировок: {state.adaptive_weights_applied}")
            print(f"   🚀 Преодолений застоя: {state.stagnation_recovery}")
            print()
            print("🎯 ПРОГРЕСС:")
            sorted_goals = sorted(EVOLUTION_GOALS.items(),
                                  key=lambda x: state.goals_progress.get(x[0], 0),
                                  reverse=True)
            for gk, gd in sorted_goals[:15]:  # Показываем не больше 15
                prog = state.goals_progress.get(gk, 0)
                star = "⭐" if gk == 'ml_ai' else "  "
                unlocked = "🔓" if gk in LOCKED_GOALS and gk in state.unlocked_goals else "  "
                weak = "⚠️" if prog < CONFIG['WEAK_CATEGORY_THRESHOLD'] else "  "
                custom = "✨" if gk.startswith('strengthen_') or gk.startswith('combine_') or gk.startswith('improve_') else "  "
                print(f"   {gd['icon']} {gd['name']:22} {self.bar(prog)} {star} {unlocked} {weak} {custom}")
            print()
            print("🧬 ГЕНЕТИКА:")
            print(f"   Паттернов: {state.code_pool_size} | Элитных: {state.elite_patterns}")
            print(f"   Застойных: {len(self.code_pool.stagnant_patterns) if hasattr(self, 'code_pool') else 0}")
            print(f"   🔗 Использований: {state.library_usage_count}")
            print(f"   🤖 ML моделей: {state.ml_models_created} | Предсказаний: {state.ml_predictions_made}")
            print(f"   🔄 Кросс-категорий: {state.cross_category_uses}")
            print(f"   🆕 META: {state.meta_evolution_count} (успех: {state.meta_evolution_success})")
            print(f"   🧬 САМО: {state.self_evolution_count} (успех: {state.self_evolution_success})")
            print(f"   📊 Инноваций: {state.innovation_score:.2f}")
            print()
            print("📊 СТАТИСТИКА:")
            sr = (state.successful_mutations / max(1, state.mutation_count)) * 100
            print(f"   Мутаций: {state.mutation_count} | Успех: {state.successful_mutations} ({sr:.1f}%)")
            print(f"   Библиотек: {len(libs)} | Функций: {len(funcs)}")
            print(f"   🔧 Исправлено: {state.fixed_syntax_errors}")
            print(f"   🧹 Очищено: {state.cleaned_libraries}")
            if state.fitness_history and len(state.fitness_history) > 1:
                last_improve = state.fitness_history[-1] - state.fitness_history[-2]
                if last_improve > 0:
                    print(f"   📈 Прирост: +{last_improve:.0f}")
            print("=" * 120)
            print(f"⚙️  ВЕСА МУТАЦИЙ: { {k: f'{v:.2f}' for k, v in state.mutation_weights.items()} }")
            print("=" * 120)

# ============================================================================
# ОПТИМИЗИРОВАННЫЙ ЭКСПОРТЁР (УЛУЧШЕННЫЙ)
# ============================================================================
class ReportExporter:
    def __init__(self, ev):
        self.ev = ev
        Path(CONFIG['REPORTS_DIR']).mkdir(exist_ok=True)

    def export_json_report(self):
        report = {
            'timestamp': datetime.now().isoformat(),
            'generation': self.ev.state.generation,
            'fitness': {
                'current': self.ev.state.current_fitness,
                'best': self.ev.state.best_fitness,
                'history': self.ev.state.fitness_history[-100:]
            },
            'code_pool': {
                'size': len(self.ev.code_pool.patterns),
                'elite': len(self.ev.code_pool.elite_patterns),
                'stagnant': len(self.ev.code_pool.stagnant_patterns) if hasattr(self.ev.code_pool, 'stagnant_patterns') else 0,
                'stats': self.ev.code_pool.get_stats()
            },
            'stats': {
                'mutations': self.ev.state.mutation_count,
                'successful': self.ev.state.successful_mutations,
                'failed': self.ev.state.failed_mutations,
                'rate': self.ev.state.successful_mutations / max(1, self.ev.state.mutation_count)
            },
            'ml_stats': {
                'models': self.ev.state.ml_models_created,
                'predictions': self.ev.state.ml_predictions_made,
                'accuracy': self.ev.state.ml_accuracy_avg,
                'library_usage': self.ev.state.library_usage_count,
                'cross_category': self.ev.state.cross_category_uses
            },
            'meta_evolution': {
                'count': self.ev.state.meta_evolution_count,
                'success': self.ev.state.meta_evolution_success
            },
            'self_evolution': {
                'count': self.ev.state.self_evolution_count,
                'success': self.ev.state.self_evolution_success
            },
            'fix_stats': {
                'fixed_errors': self.ev.state.fixed_syntax_errors,
                'cleaned_libraries': self.ev.state.cleaned_libraries
            },
            'health_stats': {
                'avg_health': self.ev.state.avg_health_score,
                'removed_broken': self.ev.state.removed_broken_libraries,
                'healed': self.ev.state.healed_libraries,
                'healing_attempts': self.ev.state.healing_attempts,
                'successful_healing': self.ev.state.successful_healing,
                'proactive_heals': self.ev.state.proactive_heals,
                'removed_unused': self.ev.state.removed_unused_libraries,
                'removed_duplicate_imports': self.ev.state.removed_duplicate_imports,
                'fixed_broken_functions': self.ev.state.fixed_broken_functions,
                'removed_dead_code': self.ev.state.removed_dead_code,
                'added_imports': self.ev.state.added_imports,
                'created_dependencies': self.ev.state.created_dependencies
            },
            'optimization_stats': {
                'balance_adjustments': self.ev.state.balance_adjustments,
                'patterns_merged': self.ev.state.patterns_merged,
                'functions_optimized': self.ev.state.functions_optimized,
                'avg_complexity': self.ev.state.avg_complexity,
                'innovation_score': self.ev.state.innovation_score,
                'performance_score': self.ev.state.performance_score
            },
            'new_features': {
                'custom_goals_created': self.ev.state.custom_goals_created,
                'meta_injections': self.ev.state.meta_injections,
                'compactions_performed': self.ev.state.compactions_performed,
                'self_healing_refactors': self.ev.state.self_healing_refactors,
                'adaptive_weights_applied': self.ev.state.adaptive_weights_applied,
                'stagnation_recovery': self.ev.state.stagnation_recovery,
                'mutation_weights': self.ev.state.mutation_weights,
                'rejected_syntax_errors': self.ev.state.rejected_syntax_errors,
                'auto_fixed_syntax': self.ev.state.auto_fixed_syntax,
                'consecutive_failures': self.ev.state.consecutive_failures
            },
            'goals': self.ev.state.goals_progress,
            'unlocked_goals': list(self.ev.state.unlocked_goals),
            'library_stats': self.ev.library_creator.get_stats(),
            'function_stats': self.ev.function_creator.get_stats(),
            'health_stats_detailed': self.ev.health_manager.get_stats(),
            'memory_stats': self.ev.memory_manager.get_stats() if hasattr(self.ev, 'memory_manager') else {},
            'compactor_stats': self.ev.code_compactor.get_stats() if hasattr(self.ev, 'code_compactor') else {},
            'injector_stats': self.ev.meta_injector.get_stats() if hasattr(self.ev, 'meta_injector') else {},
            'healer_stats': self.ev.advanced_healer.get_stats() if hasattr(self.ev, 'advanced_healer') else {},
            'goal_creator_stats': self.ev.dynamic_goal_creator.get_stats() if hasattr(self.ev, 'dynamic_goal_creator') else {}
        }
        fn = f"{CONFIG['REPORTS_DIR']}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(fn, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        logger.info(f"📄 JSON отчёт: {fn}")
        return fn

    def export_auto(self):
        if self.ev.state.generation % 50 == 0 and self.ev.state.generation > 0:
            self.export_json_report()

# ============================================================================
# ЗАПУСК
# ============================================================================
def main():
    print("\n" + "=" * 120)
    print("🤖 САМОЭВОЛЮЦИОНИРУЮЩАЯСЯ ПРОГРАММА v32.0")
    print("   🚀 КВАНТОВЫЙ СКАЧОК + ИНТЕЛЛЕКТ")
    print("   🧬 ЭВОЛЮЦИЯ КОДА ЭВОЛЮЦИИ")
    print("   🤖 ИНТЕГРИРОВАННЫЙ ML ДВИЖОК")
    print("   🎯 ДИНАМИЧЕСКОЕ СОЗДАНИЕ ЦЕЛЕЙ")
    print("   🧹 СЖАТИЕ И ОПТИМИЗАЦИЯ КОДА")
    print("   🔄 ВНЕДРЕНИЕ МЕТА-ЗНАНИЙ")
    print("   💊 АКТИВНОЕ САМОИСЦЕЛЕНИЕ")
    print("   ⚖️ АДАПТИВНАЯ БАЛАНСИРОВКА")
    print("   🔧 СИНТАКСИЧЕСКАЯ ВАЛИДАЦИЯ")
    print("   🧪 ПРЕДВАРИТЕЛЬНОЕ ТЕСТИРОВАНИЕ")
    print("=" * 120)
    print("\n📋 БАЗОВЫЕ ЦЕЛИ ЭВОЛЮЦИИ:")
    for i, (g, d) in enumerate(sorted(BASE_EVOLUTION_GOALS.items(), key=lambda x: x[1]['priority']), 1):
        star = "⭐" if g == 'ml_ai' else "  "
        print(f"   {i}. {d['icon']} {d['name']} (вес: {d['weight']}, приоритет: {d['priority']}) {star}")
    print("\n🔒 ЗАБЛОКИРОВАННЫЕ ЦЕЛИ (будут разблокированы при выполнении условий):")
    for g, d in LOCKED_GOALS.items():
        print(f"   {d['icon']} {d['name']} - условие: {d['unlock_condition']}")
    print("\n✨ ДИНАМИЧЕСКИЕ ЦЕЛИ (будут создаваться системой по мере необходимости):")
    print("   ⚡ Усиление слабых категорий")
    print("   🔄 Комбинации успешных категорий")
    print("   🤖 Повышение точности ML")
    print("   ⚡ Оптимизация производительности")
    print(f"\n⚙️  ОПТИМИЗИРОВАННЫЕ НАСТРОЙКИ:")
    print(f"   MUTATION_INTERVAL: {CONFIG['MUTATION_INTERVAL']}с")
    print(f"   QUALITY_THRESHOLD: {CONFIG['QUALITY_THRESHOLD']}%")
    print(f"   CODE_COMPACTION: {CONFIG['CODE_COMPACTION_ENABLED']}")
    print(f"   META_INJECTION: {CONFIG['META_KNOWLEDGE_INJECTION']}")
    print(f"   SELF_HEALING_REFACTOR: {CONFIG['SELF_HEALING_REFACTOR']}")
    print(f"   ADAPTIVE_WEIGHTS: {CONFIG['ADAPTIVE_MUTATION_WEIGHTS']}")
    print(f"   DYNAMIC_GOALS: {CONFIG['DYNAMIC_GOAL_CREATION']}")
    print(f"   SYNTAX_VALIDATION: {CONFIG['ENABLE_PRE_VALIDATION']}")
    print(f"   AUTO_REJECT_BROKEN: {CONFIG['AUTO_REJECT_BROKEN_SYNTAX']}")
    print(f"\n📁 ДИРЕКТОРИИ:")
    print(f"   Библиотеки: {CONFIG['LIBRARIES_DIR']}/")
    print(f"   ML модели: {CONFIG['MODELS_DIR']}/")
    print(f"   Отчёты: {CONFIG['REPORTS_DIR']}/")
    print("\n⏳ Запуск эволюции...")
    time.sleep(2)
    ev = EvolutionSystem()
    ev.run()

if __name__ == "__main__":
    main()
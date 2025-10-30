import pytest
import pandas as pd
from src.features.custom_transformers import BinaryMapper, MonthMapper

# Fixture de dados de teste
@pytest.fixture
def sample_data():
    """Cria um DataFrame de exemplo para teste dos transformadores."""
    data = {
        'binary_col': ['yes', 'no', 'yes', 'no', 'yes'],
        'month_col': ['jan', 'feb', 'mar', 'nov', 'dec'],
        'order_col': [10, 20, 30, 40, 50]
    }
    return pd.DataFrame(data)

# Teste para o BinaryMapper
def test_binary_mapper(sample_data):
    """Verifica se o BinaryMapper converte corretamente valores binários."""
    mapper = BinaryMapper()

    # Selecionando apenas a coluna que será transformada
    X = sample_data[['binary_col']]

    # Executando a transformação
    X_transformed = mapper.transform(X)

    # Valores esperados após a transformação
    expected_values = pd.DataFrame({'binary_col':[1, 0, 1, 0, 1]})

    # Assegurando que os valores transformados são iguais aos esperados
    pd.testing.assert_frame_equal(X_transformed, expected_values)

def test_binary_mapper_features_names_out():
    """Verifica se o método names_out do BinaryMapper retorna os nomes corretos das colunas."""
    mapper = BinaryMapper()
    names = ['col_A', 'col_B']
    assert mapper.get_feature_names_out(names) == names

# Teste para o MonthMapper
def test_month_mapper(sample_data):
    """Verifica se o MonthMapper converte corretamente nomes de meses em números (jan -> 1, feb -> 2, etc.)."""
    mapper = MonthMapper()

    # Selecionando apenas a coluna que será transformada
    X = sample_data[['month_col']]

    # Executando a transformação
    X_transformed = mapper.transform(X)

    # Valores esperados: ['jan: 1, 'feb': 2, 'mar': 3, 'nov': 11, 'dec': 12]
    expected_values = pd.DataFrame({'month_col':[1, 2, 3, 11, 12]}, dtype=int)

    # Igualando os índices para evitar falhas na comparação
    expected_values.index = X_transformed.index

    pd.testing.assert_frame_equal(X_transformed, expected_values)

def test_month_mapper_features_names_out():
    """Verifica se o método names_out do MonthMapper retorna os nomes corretos das colunas."""
    mapper = MonthMapper()
    names = ['month_col']
    assert mapper.get_feature_names_out(names) == names
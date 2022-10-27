import pytest
from uuid import uuid4


@pytest.fixture
def request_body():
    return {
        "assesment": {
            "tipo": "self",
            "nome": "Self Profissional",
            "jogo": "fd4d985e-b887-4a47-ac00-f646f49fcd42",
            "licenca": {
                "codigo": f"{uuid4()}",
                "perfil_dono": {
                    "nome": "Willames de Jesus Campos",
                    "email": "williames@arbache.com",
                    "codigo": f"{uuid4()}",
                },
                "perfil_jogador": {
                    "nome": "Willames de Jesus Campos",
                    "email": "williames@arbache.com",
                    "codigo": f"{uuid4()}",
                }
            },
            "rodadas": 6,
            "desafios": 32,
            "badge_jogo_nome": "Profissional De Excel\\u00eancia",
            "badge_jogo_descricao": "Teste Da badge do jogo",
            "badge_jogo_valor": -57
        },
        "descricao": {
            "progresso": 100,
            "data_inicio": "01/09/2022 17:05:46",
            "data_fim": "18/10/2022 14:51:01",
            "tempo": "0:01:45"
        },
        "comportamentos": [
            {
                "codigo": f"{uuid4()}",
                "nome": "Curioso",
                "valor": -160,
                "descricao_comportamento": "Sem descri\\u00e7\\u00e3o.",
                "comportamento_dominancia": "Tem interesse em experimentar novas ideias e novas formas de realizar as suas tarefas e n\\u00e3o se mant\\u00e9m em sua zona de conforto."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Curioso",
                "valor": -160,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Democr\\u00e1tico",
                "valor": 140,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Ouvinte",
                "valor": -210,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Prestativo",
                "valor": -210,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Acolhedor",
                "valor": 80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Integrador",
                "valor": 80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Inventivo",
                "valor": -160,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Colaborativo",
                "valor": -80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Proativo",
                "valor": 80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Vers\\u00e1til",
                "valor": 80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Pragm\\u00e1tico",
                "valor": -120,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Empoderador",
                "valor": 40,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Agregador",
                "valor": -80,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Cooperativo",
                "valor": -60,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Resiliente",
                "valor": -120,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Empoderador",
                "valor": 40,
                "descricao_comportamento": "Sem descri\\u00e7\\u00e3o.",
                "comportamento_dominancia": "Inspira a equipe, motiva seus colegas, superiores e/ou subordinados pelo exemplo e incentiva-os a aceitar movimentos e a\\u00e7\\u00f5es de desenvolvimento, fornecendo tarefas desafiadoras e permitindo a exist\\u00eancia de grupos com capacidade de di\\u00e1logo. Fornece tarefas desafiadoras e \\u201cstretching\\u201d, desenvolve um ambiente seguro e nada autorit\\u00e1rio e permite experimenta\\u00e7\\u00f5es."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Integrador",
                "valor": 80,
                "descricao_comportamento": "Sem descri\\u00e7\\u00e3o.",
                "comportamento_dominancia": "Consegue rapidamente encontrar um lugar comum e solucionar problemas para o bem de todos. Produz relacionamentos construtivos e efetivos, usando a diplomacia, e consegue acalmar situa\\u00e7\\u00f5es tensas confortavelmente."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Proativo",
                "valor": 80,
                "descricao_comportamento": "Sem descri\\u00e7\\u00e3o.",
                "comportamento_dominancia": "Busca alcan\\u00e7ar as metas da organiza\\u00e7\\u00e3o com proatividade e luta pelos pr\\u00f3prios interesses, mas mantendo o senso de justi\\u00e7a com outras pessoas e outros grupos. Encoraja a colabora\\u00e7\\u00e3o, tomando a dianteira para que sua equipe realize suas atividades, e \\u00e9 franco com os colegas."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Resiliente",
                "valor": -120,
                "descricao_comportamento": "Persiste em concluir as a\\u00e7\\u00f5es propostas, especialmente diante de resist\\u00eancia ou contratempos.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Resiliente tem persist\\u00eancia para encarar os problemas que surgem durante a realiza\\u00e7\\u00e3o de suas atividades e consegue superar resist\\u00eancias.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 Adapte seu mindset para ter um autocontrole cada vez maior e lidar positivamente com contratempos e dificuldades. \\n\\u2192 Mantenha sempre o foco em suas metas e resultados desejados e encontrar solu\\u00e7\\u00f5es para respostas negativas ou entrave \\u00e0s suas negocia\\u00e7\\u00f5es."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Integrador",
                "valor": 80,
                "descricao_comportamento": "Consegue ver oportunidades para sinergias e integra\\u00e7\\u00f5es onde a maioria n\\u00e3o v\\u00ea e \\u00e9 bom em descobrir os processos necess\\u00e1rios para solucionar problemas.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Integrador se preocupa em simplificar os processos e opera\\u00e7\\u00f5es em suas vendas, de modo que o trabalho seja feito com maior simplicidade e efici\\u00eancia.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 Analise o seu segmento de atua\\u00e7\\u00e3o de forma ampla, pois assim \\u00e9 poss\\u00edvel aproveitar as oportunidades, integrar-se a profissionais de vendas com habilidades complementares e otimizar o consumo de seus recursos."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Inventivo",
                "valor": -160,
                "descricao_comportamento": "Tem muitas ideias novas e \\u00fanicas.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Inventivo tem um perfil mais criativo e certa facilidade para criar ideias novas e consegue us\\u00e1-las bem no dia a dia de vendas.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 N\\u00e3o tenha medo de sair da rotina e explorar novas ideias e buscar novas formas de realizar suas atividades. O profissional de vendas deve se abrir para oportunidades e ideias que melhorem seus resultados e o relacionamento com clientes."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Articulado",
                "valor": -210,
                "descricao_comportamento": "Facilmente faz conex\\u00f5es com conceitos at\\u00e9 ent\\u00e3o n\\u00e3o relacionados.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Articulado demonstra ter facilidade para fazer conex\\u00f5es entre conceitos e ideias ainda n\\u00e3o relacionados e aproveitar isso nas suas atividades de vendas.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 Estude bastante sobre diversos temas, de modo a ampliar seus conhecimentos e se abrir para novas possibilidades. Quanto maior o universo de informa\\u00e7\\u00f5es que um(a) profissional de vendas possui, maior a chance de ele(a) explorar sua criatividade e criar estrat\\u00e9gias de vendas inovadoras e eficientes, que v\\u00e3o conquistar qualquer tipo de cliente."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Curioso",
                "valor": -160,
                "descricao_comportamento": "Interessa-se por novas ideias e novas formas de fazer suas tarefas.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Curioso demonstra maior interesse por novas ideias e em como elas podem ajudar a encontrar novas e melhores formas de realizar suas atividades e atingir suas metas de vendas.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 Aproveite toda fonte de informa\\u00e7\\u00e3o para aprender e ter novas ideias: cr\\u00edticas, feedbacks, livros, reuni\\u00f5es, conversas com clientes ou amigos, etc. A curiosidade nos permite ver a profiss\\u00e3o com outros olhos, formular melhores estrat\\u00e9gias de negocia\\u00e7\\u00e3o e conquistar mais clientes."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Prestativo",
                "valor": -210,
                "descricao_comportamento": "\\u00c9 dedicado a encontrar as expectativas e requerimentos de clientes internos e externos.",
                "comportamento_dominancia": "O(a) profissional que domina o comportamento Prestativo busca intensamente entender quais s\\u00e3o as expectativas de seus clientes internos e externos, para conseguir fazer boas vendas e auxili\\u00e1-los no processo de compra ou em suas tomadas de decis\\u00e3o.\\nPara voc\\u00ea continuar se desenvolvendo:\\n\\u2192 Analise atentamente os requerimentos de seus clientes e estabele\\u00e7a formas e rotinas de contato. Desta forma, voc\\u00ea estar\\u00e1 sempre alinhado(a) \\u00e0s necessidades atualizadas dos clientes."
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Articulado",
                "valor": -210,
                "descricao_comportamento": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable",
                "comportamento_dominancia": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."
            }
        ],
        "competencias": [
            {
                "codigo": f"{uuid4()}",
                "nome": "Criatividade E Inova\\u00e7\\u00e3o",
                "valor": -152,
                "descricao_competencia": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                "comportamentos": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Curioso"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Inventivo"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Colaborativo"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Articulado"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Conectividade",
                "valor": 10,
                "descricao_competencia": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                "comportamentos": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Democr\\u00e1tico"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Empoderador"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Agregador"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Cooperativo"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Adaptabilidade",
                "valor": -20,
                "descricao_competencia": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                "comportamentos": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Proativo"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Vers\\u00e1til"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Pragm\\u00e1tico"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Resiliente"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "nome": "Empatia E Foco No Cliente",
                "valor": -65,
                "descricao_competencia": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                "comportamentos": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Ouvinte"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Prestativo"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Acolhedor"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Integrador"
                    }
                ]
            }
        ],
        "badges": [
            {
                "codigo": f"{uuid4()}",
                "valor": -57,
                "nome": "Profissional De Excel\\u00eancia",
                "descricao": "Profissional De Excel\\u00eancia",
                "competencias": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Empatia E Foco No Cliente"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Criatividade E Inova\\u00e7\\u00e3o"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Adaptabilidade"
                    },
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Conectividade"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "valor": -65,
                "nome": "Empatia E Foco No Cliente",
                "descricao": "Empatia E Foco No Cliente",
                "competencias": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Empatia E Foco No Cliente"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "valor": 10,
                "nome": "Conectividade",
                "descricao": "Conectividade",
                "competencias": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Conectividade"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "valor": -20,
                "nome": "Adaptabilidade",
                "descricao": "Adaptabilidade",
                "competencias": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Adaptabilidade"
                    }
                ]
            },
            {
                "codigo": f"{uuid4()}",
                "valor": -152,
                "nome": "Criatividade E Inova\\u00e7\\u00e3o",
                "descricao": "Criatividade E Inova\\u00e7\\u00e3o",
                "competencias": [
                    {
                        "codigo": f"{uuid4()}",
                        "nome": "Criatividade E Inova\\u00e7\\u00e3o"
                    }
                ]
            }
        ]
    }


@pytest.fixture
def response_BAD_REQUEST():
    return {
        "badges": {
            "0": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            },
            "1": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            },
            "3": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            },
            "4": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            }
        },
        "competencias": {
            "0": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            },
            "2": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            },
            "3": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a 0."
                ]
            }
        },
        "comportamentos": {
            "0": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "1": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "2": {
                "valor": [
                    "Certifique-se de que este valor seja inferior ou igual a 100."
                ]
            },
            "3": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "4": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "7": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "11": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "15": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "19": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "21": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "22": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "23": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "24": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            },
            "25": {
                "valor": [
                    "Certifque-se de que este valor seja maior ou igual a -100."
                ]
            }
        }
    }


@pytest.fixture
def response_OK():
    return {
        "codigo": f"{uuid4()}",
        "jogador": {
            "codigo": f"{uuid4()}",
            "nome": "Willames de Jesus Campos",
            "email": "williames@arbache.com"
        },
        "equipe": None,
        "data_selecao_jogador": None,
        "dono": True,
        "liberado_por": {
            "codigo": f"{uuid4()}",
            "nome": "Willames de Jesus Campos",
            "email": "teste@arbache.com"
        },
        "url": "marketplace",
        "validade": "18/01/2023",
        "data_inicio": "01/09/2022 17:05:46",
        "data_conclusao": "01/09/2022 14:12:01",
        "jogo": {
            "codigo": f"{uuid4()}",
            "nome": "Self Profissional"
        },
        "configuracao": None
    }

{% if current_user.is_authenticated %}
                    <a class="nav-link" href="/logout">{{ current_user.name }}</a>
                    {% else %}
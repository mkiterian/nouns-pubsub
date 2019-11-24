import json
from kafka import KafkaProducer

from get_nouns import get_all_icons, get_icon_groups

if __name__ == '__main__':
    items = ['fish', 'dog', 'cat', 'bird']
    icons = get_all_icons(items)
    if icons:
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        grouped_icons = get_icon_groups(icons)

        for key in grouped_icons:
            for icon in grouped_icons[key]:
                key_bytes = bytes(icon['id'], encoding='utf-8')
                value_bytes = bytes(json.dumps(icon), encoding='utf-8')
                producer.send(key, key=key_bytes, value=value_bytes)
                producer.flush()
                print('Successfully produced!!')
                

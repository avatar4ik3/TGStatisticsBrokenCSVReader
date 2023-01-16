# Установа

скачайте [файл](https://github.com/avatar4ik3/TGStatisticsBrokenCSVReader/releases/tag/release)

переместите его в удобную вам папку

добавьте путь до этой папки в Path [как это сделать](<https://learn.microsoft.com/ru-ru/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)>)

# Использование

## Поддерживаемые флаги

    -h , --help - вывод помощи на экран

    -i, --input - .csv файл, который необходимо обработать

    -o , --output - имя выводимого файла. его расширение будет установлено программой. Значение по умолчанию "output"

    --parce , --no-parce - флаги, указывающие на необходимость парсить дату из переданного файла. Использовать если есть какие-то проблемы. Если не указан используется --no-parce

## Пример использования

```console
    tgs2xls -i my_input_file.csv -o my_output_file --no-parce
```

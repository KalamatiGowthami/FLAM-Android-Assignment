#include <iostream>
#include <vector>
#include <list>

class MyHashMap
{
private:
    struct KeyValue
    {
        int key;
        int value;
        KeyValue(int k, int v) : key(k), value(v) {}
    };

    static const int TABLE_SIZE = 10007;

    std::vector<std::list<KeyValue>> buckets;

    int hash(int key)
    {
        const int kMul = 2654435769;
        return ((static_cast<unsigned long long>(key) * kMul) >> 16) % TABLE_SIZE;
    }

public:
    MyHashMap()
    {
        buckets.resize(TABLE_SIZE);
    }

    void put(int key, int value)
    {
        int index = hash(key);
        auto &bucket = buckets[index];

        for (auto &pair : bucket)
        {
            if (pair.key == key)
            {
                pair.value = value; // update existng key
                return;
            }
        }

        // key not found, insert new pair
        bucket.emplace_back(key, value);
    }

    int get(int key)
    {
        int index = hash(key);
        auto &bucket = buckets[index];

        for (auto &pair : bucket)
        {
            if (pair.key == key)
            {
                return pair.value;
            }
        }

        return -1; // Key not found
    }

    void remove(int key)
    {
        int index = hash(key);
        auto &bucket = buckets[index];

        for (auto it = bucket.begin(); it != bucket.end();)
        {
            if (it->key == key)
            {
                it = bucket.erase(it); // erase returns the next valid iterator
                return;
            }
            else
            {
                ++it;
            }
        }
    }
};

// Simple test
int main()
{
    MyHashMap *myHashMap = new MyHashMap();
    myHashMap->put(1, 1);
    myHashMap->put(2, 2);
    std::cout << myHashMap->get(1) << std::endl;
    std::cout << myHashMap->get(3) << std::endl;
    myHashMap->put(2, 1);
    std::cout << myHashMap->get(2) << std::endl;
    myHashMap->remove(2);
    std::cout << myHashMap->get(2) << std::endl;

    delete myHashMap;
    return 0;
}

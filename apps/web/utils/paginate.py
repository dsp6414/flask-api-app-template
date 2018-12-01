
def paginate2dict(paginate):
    return {
        "items": [item.to_dict() for item in paginate.items],
        "items_size": len(paginate.items),
        "current_page": paginate.page,  # 当前页数
        "total_pages": paginate.pages,  # 总页数
        "has_prev": paginate.has_prev,  # 是否有前一页
        "has_next": paginate.has_next,  # 是否有下一页
        "prev_number": paginate.prev_num,   # 前一页数
        "next_number": paginate.next_num,   # 后一页数
    }